# Profile_Name
# Job_Title
# Company_Name
# Location
# Education
# Skills
# Profile_URL
# Followers




from playwright.sync_api import sync_playwright
import streamlit as st
import time
import pandas as pd
from io import BytesIO
import plotly.express as px
from datetime import datetime

URL = "https://www.linkedin.com/login"

def linkedin_Profile_Lead_Generation(email, password, profiles_to_scrape_name):
    data_scraped = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        # Open a new page in incognito mode
        page = context.new_page()
        # page = browser.new_page()
        page.goto(URL)
        
        time.sleep(2)
        
        profiles_hrefs = []
            
        
        
        page.locator("input#username").fill(email)
        page.locator("input#password").fill(password)
        page.locator("button[type='submit']").click()
        
        time.sleep(30)
        
        page.locator("input[type='text']").first.fill(profiles_to_scrape_name)
        
        page.locator("input[type='text']").first.press("Enter")
        
        
        time.sleep(10)
        
        page.get_by_text("See all people results", exact=True).first.click()
        
        
        up = True
        
        while up:
            
            time.sleep(10)
            
            one_page_profiles_container = page.locator("ul[role='list']")
            
            if one_page_profiles_container:
                page_profiles = one_page_profiles_container.locator("a.app-aware-link ").all()

                print(len(page_profiles))
                
                for profile in page_profiles:
                    href = profile.get_attribute("href")
                    profiles_hrefs.append(href)
                    print(href)
                    
            
            if page.locator('button.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--1.artdeco-button--tertiary.ember-view.artdeco-pagination__button.artdeco-pagination__button--next').count() > 0:
                
                page.locator('button.artdeco-button.artdeco-button--muted.artdeco-button--icon-right.artdeco-button--1.artdeco-button--tertiary.ember-view.artdeco-pagination__button.artdeco-pagination__button--next').click()
                
                
            else:
                
                up = False
        
                
                
            
        
        
        # page.wait_for_selector('ul.css-zu9cdh.eu4oa1w0', timeout=10000)
        # time.sleep(5)
        # up = True
        # jobs_hrefs = []
        # test_phase_page_count = 0
        # while up:
        #     time.sleep(5)
        #     if test_phase_page_count == 3:
        #         up=False
                
    
        #     if page.get_by_role("checkbox").count()>0:
        #         page.get_by_role("checkbox").click()
        #     print("Passed 2")
        #     page.wait_for_selector('ul.css-zu9cdh.eu4oa1w0', timeout=10000)
        #     time.sleep(5)
        #     page_job_container = page.locator('ul.css-zu9cdh.eu4oa1w0')
        #     job_items = page_job_container.locator('li.css-5lfssm.eu4oa1w0').all()
        #     print(f"Found {len(job_items)} job items.")
        #     jobs = [item.locator("a.jcs-JobTitle.css-jspxzf.eu4oa1w0") for item in job_items if item.locator("a.jcs-JobTitle.css-jspxzf.eu4oa1w0").count() > 0]
        #     if jobs:
        #         for item in jobs:
        #             href = item.get_attribute("href")
        #             href = URL + href
        #             jobs_hrefs.append(href)
        #     try:
        #         if page.get_by_label("Next Page").count() > 0:
        #             page.get_by_label("Next Page").click() 
        #             test_phase_page_count += 1
        #             time.sleep(3)
        #             if page.locator("button.css-yi9ndv.e8ju0x51").count() > 0:
        #                 page.locator("button.css-yi9ndv.e8ju0x51").click() 
        #         else:
        #             up = False
        #             print("No more pages available.")
        #     except Exception as e:
        #         up = False
        #         print(f"An error occurred: {e}")
                
        # Profile_Name
        # Job_Title
        # Company_Name
        # Location
        # Education
        # Skills
        # Profile_URL     
        # if len(jobs_hrefs)>0:
        #     for job_link in jobs_hrefs:
        #         page.goto(job_link)
        #         time.sleep(3)      
        #         job_url = page.url
        #         if page.locator("h1.jobsearch-JobInfoHeader-title.css-1b4cr5z.e1tiznh50").count() > 0:
        #             Job_Title = page.locator("h1.jobsearch-JobInfoHeader-title.css-1b4cr5z.e1tiznh50").inner_text()
        #         if page.locator("a.css-1ioi40n.e19afand0").count() > 0:
        #             Company_Name = page.locator("a.css-1ioi40n.e19afand0").inner_text()
        #             Company_Website = page.locator("a.css-1ioi40n.e19afand0").get_attribute("href")
        #         if page.locator("div.css-45str8.eu4oa1w0").count() > 0:
        #             Location = page.locator("div.css-45str8.eu4oa1w0").inner_text()
        #         if page.locator('#jobDescriptionText').count() > 0:
        #             Full_Job_Info = page.locator('#jobDescriptionText').inner_text()

        #         row = [Job_Title, Company_Name, Company_Website, Location, Full_Job_Info]
                
        #         data_scraped.append(row)
                
                    
                    
        time.sleep(5)
        page.close()
        browser.close()
        
    return data_scraped
    
if __name__ == "__main__":
    
    # Profile_Name
    # Job_Title
    # Company_Name
    # Location
    # Education
    # Skills
    # Profile_URL
    # Followers
    
    HEADERS = ["PROFILE NAME", "JOB TITLE", "COMPANY NAME", "LOCATION", "EDUCATION", "SKILLS", "PROFILE_URL", "FOLLOWERS"]
    
    st.title("Welcome to Profiles Lead Generation from Linkedin Web app")
    
    Email = st.text_input("# EMAIL", "example@gmail.com")
    
    Password = st.text_input("# PASSWORD", "****************")
    
    
    if Email  == "example@gmail.com":
        st.warning("# Please enter your email address")
    
    if Password == "****************":
        st.warning("Please enter your password")
    
    data_scraped = []
    
    df = pd.DataFrame(data=data_scraped, columns=HEADERS)
    
    
    if Email!="example@gmail.com" and Password!="****************":
        
        profile_name = st.text_input("Enter the profile that you want to scrape name")
        # Downloaded data filtered as csv files
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            if st.button(f'Scrape all {profile_name} profiles from linkedin social media'):
                with st.spinner("Load ..."):
                    try:
                        data_scraped = linkedin_Profile_Lead_Generation(Email, Password, profile_name)
                    except Exception as e:
                        st.error(f"An error occurred during scraping: {e}")  
                st.info(f'{len(data_scraped)} profiles found')
                st.success("Data scraped successfully")  
                        
        with col2:
            
            if len(data_scraped)!=0:
                
                df = pd.DataFrame(data = data_scraped, columns = HEADERS)
            
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download the dataset as CSV",
                    data=csv,
                    file_name=f'{profile_name}-{datetime.now()}.csv',
                    mime='text/csv'
                )
                
            else:
                pass
                
        with col3:
            
            if len(data_scraped)!=0:
                
                df = pd.DataFrame(data = data_scraped, columns = HEADERS)
                
                # Create an Excel file in memory
                output = BytesIO()
                writer = pd.ExcelWriter(output, engine='xlsxwriter')
                df.to_excel(writer, index=False)
                writer.close()
                xlsx_data = output.getvalue()
                
                
                # xlsx = df.to_excel(index=False).encode('utf-8')
                # Provide the download button
                st.download_button(
                    label="Download the dataset as xlsx",
                    data=xlsx_data,
                    file_name=f'{profile_name}-{datetime.now()}.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )
                
            else:
                pass
            

        if not df.empty:
            view_df_as_table = st.checkbox("View the dataset as a table", key="one")
            
            if view_df_as_table:
                st.table(df)
        else:
            pass
            
   
    
    
    
    
    
    
    
        
    
    
        
    
    
    
    

        
    