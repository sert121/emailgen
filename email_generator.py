import streamlit as st
import requests
import json
import random
from dotenv import load_dotenv
import os 

load_dotenv()

PAGE_1 = "Email Generator"
PAGE_2 = "Reverse engineering emails"

API_KEY = st.secrets["API_KEY_DEF"]

st.sidebar.title("Genmail.ai")
navigation = st.sidebar.radio("Features", options=[PAGE_1, PAGE_2])

def open_ai_call(prompt,max_tokens=300):
        response = requests.post(
            "https://api.openai.com/v1/completions",
            headers={"Authorization": "Bearer " + API_KEY,
                    "Content-Type": "application/json"},
            data=json.dumps({
                'model':'text-davinci-002',
                'prompt': prompt,
                'max_tokens': max_tokens,
                'temperature': 0.7,
                'top_p': 1,
                'frequency_penalty': 0,
                'presence_penalty': 0,
            })) 
        resp1 = response.json()
        try:
            generated_text = resp1['choices'][0]['text']
        except:
            generated_text = "Sorry, we are unable to generate an email for you at the moment. You might have exceeded the number of trial API calls."
        return generated_text

if navigation == PAGE_1:
    st.header("Email Generator 🚀💭")
    st.info("Generate customized personal email templates to save time and effort on those boring emails.")
    page_1_options = ["Marketing", "Business","Sales", "Co-Founder", "Recruiting",]
    selected_option = st.selectbox("Choose your domain", options=page_1_options)
    if selected_option == "Marketing":
        # wati for user input
        company_name = st.text_input("Company name",placeholder="Google")
        company_bio = st.text_input("Company Bio",placeholder="Google is a tech company that specializes in search engines")
        prompt = f"Suggest 20 creative headers while writing an email for a marketing campaign for {company_name}"
        topic = st.text_input("Topic",value="",placeholder="Elaborate on the topic of the email ", help="Mentioning the topic will help us generate a better email")
        opener = st.text_input("Header",value="",help="If you don't enter an email header, we will generate one for you")
        generated_email = ""
        st.session_state.generated_email = ''
        # generating a list of openers using openAI
     
        if st.button("Generate Email"):

            if opener=="":
                generated_openers = open_ai_call(prompt)
                list_generated_openers = generated_openers.split("\n")
                # pick random element from the list
                random_opener = random.choice(list_generated_openers)
                prompt_for_email = f'''Generate a detailed marketing email using the company's bio , topic and header provided below. 
                Imagine you are a marketing specialist employee at Google who is endorsing the company's product to its customer, so be as creative as possible while staying true to the company's brand.
                Also try to get attention of the reader by making the content of the email interesting.

                Company's Bio: {company_bio}
                Email Header: {random_opener}
                Topic for the email: {f"Marketing campaign for {company_name}" if topic == "" else topic}
                '''
            if opener != "":
                prompt_for_email = f'''Generate a detailed marketing email using the company's bio, topic and header provided below. 
                Imagine you are a marketing specialist employee at Google who is endorsing the company's product to its customer, so be as creative as possible while staying true to the company's brand.
                Also try to get attention of the reader by making the content of the email interesting.
                Company's Bio: {company_bio}
                Topic for the email: {f"Marketing campaign for {company_name}" if topic == "" else topic}
                Email Header: {opener}
                '''     
            with st.spinner("Generating your email..."):
                generated_email = open_ai_call(prompt_for_email,300)
                generated_email = open_ai_call(prompt_for_email,300)
                st.write(f'''{generated_email} 
        ''')


    elif selected_option == "Business":
        company_name = st.text_input("Company name",placeholder="Google")
        company_bio = st.text_input("Company Bio",placeholder="Google is a tech company that specializes in search engines")
        prompt = f"Suggest 20 creative headers while writing an email as a business consultant for {company_name}"
        topic = st.text_input("Topic",value="",placeholder="Elaborate on the topic of the email ", help="Mentioning the topic will help us generate a better email")
        opener = st.text_input("Header",value="",help="If you don't enter an email header, we will generate one for you")
        generated_email = ""
        st.session_state.generated_email = ''
        # generating a list of openers using openAI
     
        if st.button("Generate Email"):
            if opener=="":
                generated_openers = open_ai_call(prompt)
                list_generated_openers = generated_openers.split("\n")
                # pick random element from the list
                random_opener = random.choice(list_generated_openers)
                prompt_for_email = f'''Generate a detailed business email using the company's bio , topic and header provided below. 
                Imagine you are a top business consultant at {company_name} who is writing the email for a client, so be as creative as possible while staying true to the company's brand.
                Maintain a professional tone while writing the email. Try to get attention of the reader by making the content of the email interesting.

                Company's Bio: {company_bio}
                Email Header: {random_opener}
                Topic for the email: {f"Business email for {company_name}" if topic == "" else topic}
                '''
            if opener != "":
                prompt_for_email = f'''Generate a detailed business email using the company's bio , topic and header provided below. 
                Imagine you are a top business consultant at {company_name} who is writing the email for a client, so be as creative as possible while staying true to the company's brand.
                Maintain a professional tone while writing the email. Try to get attention of the reader by making the content of the email interesting.

                Company's Bio: {company_bio}
                Email Header: {opener}
                Topic for the email: {f"Business email for {company_name}" if topic == "" else topic}
                '''
            with st.spinner("Generating your email..."):
                generated_email = open_ai_call(prompt_for_email,300)
                st.snow()
                st.write(f'''{generated_email} 
        ''')
        
    elif selected_option == "Co-Founder":
        company_name = st.text_input("Company name",placeholder="Google")
        company_bio = st.text_input("Company Bio",placeholder="Google is a tech company that specializes in search engines")
        prompt = f"Suggest 20 creative headers while writing an email as a cofounder for {company_name}"
        topic = st.text_input("Topic",value="",placeholder="Elaborate on the topic of the email ", help="Mentioning the topic will help us generate a better email")
        opener = st.text_input("Header",value="",help="If you don't enter an email header, we will generate one for you")
        generated_email = ""
        st.session_state.generated_email = ''
        # generating a list of openers using openAI
     
        if st.button("Generate Email"):

            if opener=="":
                generated_openers = open_ai_call(prompt)
                list_generated_openers = generated_openers.split("\n")
                # pick random element from the list
                random_opener = random.choice(list_generated_openers)
                prompt_for_email = f'''Generate a detailed email using the company's bio , topic and header provided below. 
                Imagine you are a co-founder at an amzing company {company_name} who is writing the email for a potential audience, so be as creative as possible while staying true to the company's brand.
                Maintain a professional tone while writing the email. Try to get attention of the reader by making the content of the email interesting.

                Company's Bio: {company_bio}
                Email Header: {random_opener}
                Topic for the email: {f"Cofounder's email for the customers of {company_name}" if topic == "" else topic}
                '''
            if opener != "":
                # pick random element from the list
                prompt_for_email = f'''Generate a detailed email using the company's bio , topic and header provided below. 
                Imagine you are a co-founder at an amzing company {company_name} who is writing the email for a potential audience, so be as creative as possible while staying true to the company's brand.
                Maintain a professional tone while writing the email. Try to get attention of the reader by making the content of the email interesting.

                Company's Bio: {company_bio}
                Email Header: {opener}
                Topic for the email: {f"Cofounder's email for the customers of {company_name}" if topic == "" else topic}
                '''
            with st.spinner("Generating your email..."):
                generated_email = open_ai_call(prompt_for_email,300)
                st.snow()
                st.write(f'''{generated_email} 
        ''')
    elif selected_option == "Sales":
        company_name = st.text_input("Company name",placeholder="Google")
        company_bio = st.text_input("Company Bio",placeholder="Google is a tech company that specializes in search engines")
        prompt = f"Suggest 20 creative headers while writing an email as a sales agent for {company_name}"
        topic = st.text_input("Topic",value="",placeholder="Elaborate on the topic of the email ", help="Mentioning the topic will help us generate a better email")
        opener = st.text_input("Header",value="",help="If you don't enter an email header, we will generate one for you")
        generated_email = ""
        st.session_state.generated_email = ''
        # generating a list of openers using openAI
     
        if st.button("Generate Email"):

            if opener=="":
                generated_openers = open_ai_call(prompt)
                list_generated_openers = generated_openers.split("\n")
                # pick random element from the list
                random_opener = random.choice(list_generated_openers)
                prompt_for_email = f'''Generate a detailed email as a sales employee using the company's bio , topic and header provided below. 
                Imagine you are a top-performing sales employee at {company_name} who is writing the email for a potential audience, so be as creative as possible while staying true to the company's brand.
                Make the email quirky yet sellable. Try to get attention of the reader by making the content of the email interesting.

                Company's Bio: {company_bio}
                Email Header: {random_opener}
                Topic for the email: {f"Sales outreach campaign for the customers of {company_name}" if topic == "" else topic}
                '''
            if opener != "":
                prompt_for_email = f'''Generate a detailed email as a sales employee using the company's bio , topic and header provided below. 
                Imagine you are a top-performing sales employee at {company_name} who is writing the email for a potential audience, so be as creative as possible while staying true to the company's brand.
                Make the email quirky yet sellable. Try to get attention of the reader by making the content of the email interesting.

                Company's Bio: {company_bio}
                Email Header: {opener}
                Topic for the email: {f"Sales outreach campaign for the customers of {company_name}" if topic == "" else topic}
                '''
            with st.spinner("Generating your email..."):
                generated_email = open_ai_call(prompt_for_email,300)
                st.snow()
                st.write(f'''{generated_email} 
        ''')
    elif selected_option == "Recruiting":
        company_name = st.text_input("Company name",placeholder="Google")
        company_bio = st.text_input("Company Bio",placeholder="Google is a tech company that specializes in search engines")
        prompt = f"Suggest 20 creative headers while writing an email as a recruiter for {company_name}"
        topic = st.text_input("Topic",value="",placeholder="Elaborate on the topic of the email, and what you expect ", help="Mentioning the topic will help us generate a better email")
        opener = st.text_input("Header",value="",help="If you don't enter an email header, we will generate one for you")
        generated_email = ""
        st.session_state.generated_email = ''
        # generating a list of openers using openAI
     
        if st.button("Generate Email"):

            if opener=="":
                generated_openers = open_ai_call(prompt)
                list_generated_openers = generated_openers.split("\n")
                # pick random element from the list
                random_opener = random.choice(list_generated_openers)
                prompt_for_email = f'''Generate a detailed email using the company's bio , topic and header provided below. 
                Imagine you are a recruiter at an amzing company {company_name} who is writing the email for a potential employee, so highlight the benefits of working at {company_name} while staying true to the company's brand.
                Maintain a professional tone while writing the email. Elaborate on the culture and fit a bit. Try to get attention of the reader by making the content of the email interesting.

                Company's Bio: {company_bio}
                Email Header: {random_opener}
                Topic for the email: {f"Recruiter's email for potential employees of {company_name}" if topic == "" else topic}
                '''
            if opener != "":
                prompt_for_email = f'''Generate a detailed email using the company's bio , topic and header provided below. 
                Imagine you are a recruiter at an amzing company {company_name} who is writing the email for a potential employee, so highlight the benefits of working at {company_name} while staying true to the company's brand.
                Maintain a professional tone while writing the email. Elaborate on the culture and fit a bit. Try to get attention of the reader by making the content of the email interesting.

                Company's Bio: {company_bio}
                Email Header: {opener}
                Topic for the email: {f"Recruiter's email for potential employees of {company_name}" if topic == "" else topic}
                '''
            with st.spinner("Generating your email..."):
                generated_email = open_ai_call(prompt_for_email,300)
                st.snow()
                st.write(f'''{generated_email} 
        ''')



if navigation == PAGE_2:
    st.header("Reverse-Engineering Emails 🔄")
    st.info("Reverse engineer a non-ai generated email to understand the context/prompt that could be used to generate the email")
    email_info = st.text_area("Input Email", key="email")
    if st.button("Reverse Engineer Email"):
        prompt = f'''
        ------------------Email 1 ------------------
        EMAIL: Dear Alumni, I hope you all are well. 
        I am looking to get in touch with individuals working at firms such as KPMG, Deloitte, E&Y, Boston Consulting Group, World Resources Institute, (and similar firms,) who might be familiar with or are working with Knowledge management systems and software. 
        I am currently archiving the digital assets of the Council on Energy, Environment and Water (CEEW).
        CEEW is one of Asia’s leading not-for-profit policy research institutions and one of the world’s leading climate think tanks.
        I have attached a detailed description of CEEW in this email. We are looking to understand the Knowledge Management Systems that you might be working with.
        It would be great if we can connect to help us understand how we can use KMS to best benefit. 
        Cheers,

        PROMPT for email: Write a detailed email to the alumni council describing the companies you have worked for and the knowledge management systems you have worked with, while 
        asking for potential leads for your company to understand how they can use KMS to best benefit.
        ---
        ------------------Email 2 ------------------
        EMAIL: Dear Team, I hope you’re well! 
        If you’re a writer seeking to build a consistent practice within a community of diverse creatives, here’s an opportunity for you! Aditi Rao is opening subscriptions to “Committing to Your Writing Practice” which will offer a wealth of resources to develop your craft including including live writing workshops, instructional videos and reading recommendations, community discussions on creative processes, opportunities for peer feedback, and publishing suggestions! Through office hours and monthly challenges, you will be provided access to an enriching environment to sustain your growth. To learn more about our award winning instructor, and her work, you can visit: https://aditirao.net/committing-to-your-writing-practice. Aditi’s pedagogy  intentionally nudges you towards creative experimentation. She helps you visualise the possibilities in your own work and materialise them with interactive guidance from a vibrant community. Subscriptions are open till 30th January, 2023. 
        Sign up now and let's create together! 
        Warm regards, 
        
        PROMPT for email: Write a detailed email to a potential client informing them of a new opportunity for writers to join a community of creatives and build a consistent writing practice.
        ---
        ------------------Email 3 ------------------
        EMAIL: {email_info}

        PROMPT for email: 
        '''


        with st.spinner("Reverse Engineering Email..."):
            generated_response = open_ai_call(prompt, 1000)
            st.snow()
            st.write(f'''{generated_response}''')
