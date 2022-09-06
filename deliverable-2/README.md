# Lexata

## Description 

Our application aims to provide users with a straightforward way of analyzing environmental risk factors from a business and/or legal perspective. Similar to Google, our application allows for users to submit a query to be compared to a collection of data stored in our database, which will subsequently return relevant and related risk factors. A risk factor is defined as something which poses potential dangers or cause for concern, so in the context of this application, we are helping users address their questions about environmental concerns. These are described by publicly traded companies on their annual 10K forms which are submitted to the SEC. The key usage of our application is to automate the process of parsing these documents in order to answer a general question related to the topic. This process is historically time consuming and existing tools used to automate the process either rely on keyword matching or reference outdated documents. Because our application uses leading edge AI, we are able to extract data based off of relevance to an entered query without relying on specific words matching, all while saving time compared to the historic and outdated approaches to the problem.

## Key Features

Lexata’s comprehensible website design caters to the average user with simple but practical features. The homepage of the website provides relevant background information about Lexata as a company and its provided services. Engaging imagery and cogent language allow for an easy-to-use interface that is well designed and simple to navigate, particularly for a new user. The navigation bar and footer of the website are other features of interest where a user may easily navigate to the information they need, including Lexata’s search functionality and copyright notice. Perhaps the most important feature of the website is the search page and associated search bar that can be reached through the navigation bar. The search bar gives users the opportunity to query for any risk factors using simple and non-technical language which alleviates the confusion related to understanding dense legalese. Upon entering a query, the search page displays twenty results in order of significance to the user in a concise manner. Each returned risk factor is paired with its accompanying company and a read-more button so a user may locate more information if needed and effortlessly skim through the results to identify the ones most applicable to their situation. Lastly, the contact page opens an easy method of communication between the user and the company. Overall, the current features of the website provide a decluttered and streamlined user experience for an accessible and practical querying process.

## Instructions
 
A user can first arrive on the landing page with this link: https://lexata.herokuapp.com/. To query for related risk factors, begin by navigating to the search page through the navigation bar located in the top left corner of the webpage. Enter a topic of interest using the search bar and press search to query for related risk factors. Example query topics include natural disasters, importing materials, greenhouse gas emissions, insurance etc.  This will generate twenty risk factors in order of significance. Each risk factor has an associated title that is the company’s name and a read more button if a user wishes to expand the query result. 

A user may also wish to contact the company. This can be done by arriving at the contacts page through the navigation bar. This loads a form in which a user may enter the required information (name, email, organization, message) and send the form using the send button.

 
 ## Development requirements

**Server Setup**

You will need the following:

1. python 3.10 installed
2. OpenAI api key (to obtain OpenAI api key, you must make an account on the OpenAI website found here: https://openai.com/)

 Instructions to run the server (ensure that you are in the folder located at pathname: team-project-4-lexata-inc\deliverable-2\lexata-code\application):
 
 1. Set up a virtual environment with `python3 -m venv venv`
 2. Activate virtual environment with `venv\Scripts\activate` on windows or `source venv/bin/activate` on mac or linux.
 3. Run `pip install -r requirements.txt` to install dependencies. 
 4. Create a .env file in the in same directory with the following contents:
 ```
 FLASK_APP=app.py                                                                                                                                     
 FLASK_ENV=development
 open-ai-api-key = '<enter your open ai api key here>'
 mongo-url = 'mongodb+srv://<username>:<password>@cluster0.gwdwd.mongodb.net/lexata?retryWrites=true&w=majority'
 ```
 You may use the following credentials to access the database for reading. Subsitute them in for `<username>` and `<password>` in the url above.
- username: `lexata-user-1`
- password: `A4SvOmk2VY0dKxzh`
 
 5. Run the server with `python3 server.py`.
 
 **Frontend Setup**
 
 You will need the following:
 
 1. Node.js
 2. npm
 
 Instructions to run the frontend:
 1. Run the following commands to run the website while in the frontend folder found at: team-project-4-lexata-inc\deliverable-2\lexata-code\application\frontend
 ```
 npm install
 npm start
 ```
 2. To reach the website, go to http://localhost:3000.
 
 **Database Setup**
 
 This area of the code, located in the data-scripts folder, is not required to run the website. For more information, please the README.md file in team-project-4-lexata-inc\deliverable-2\lexata-code\data-scripts.
 
 ## Deployment and Github Workflow

Early on in the project preparation phase, our team divided up generalized tasks according to member's skillsets and prerequisite understandings of the software development cycle. In a broad scope, these were work in the following sections: Frontend, Backend, Scripting, and Databases. Our team stuck to this structure and organized tasks on Trello on a first come first serve basis. Because of individuals claiming tasks, it made the overall workflow process organized and allowed everyone to implement their own functionalities on their own branches. These branches included a branch for integrating Open-AI, a branch for our backend module, a branch for our scripts, and a deployment based branch. Upon being completed, each branch was merged with the 'Develop' branch using a pull request. All members that were involved in that section of the project were required to approve the pull-request before the person who created the pull request could merge it.

Because our current project is moreso a mockup rather than a consumer grade MVP, we are deploying our application on Heroku temporarily. In future iterations, we will most likely consult our partner and either make use of Microsoft Azure or AWS. Deploying to Heroku was also a process the entire group was familiar with as we have used it for many other projects outside of the course. Heroku's structure also allows for on-the-fly bug fixes and makes testing the application a lot easier versus locally hosting the app through constantly having to load up environments or servers ourselves.

 ## Licenses 

Our project is unlicensed as the ownership and usage of the software is restricted to the company itself. Usage of the code is proprietary in the sense that usage of the application (but not actual access to the code) will be granted on a subscription basis, similar to products such as Microsoft Office 365.
