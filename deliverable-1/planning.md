# Lexata Inc. - TeamName0

## Product Details
 
#### Q1: What are you planning to build?

 Most professional work today has become data-driven, becoming highly dependent on top-quality research and seamless availability of information. Issues such as technical and logistical barriers to information access are especially profound in the legal field. Trying to obtain accurate, detailed rules regarding topics such as corporate matters consumes a significant amount of time for users such as research lawyers, regulators, and students. It is often too difficult for someone to find laws themselves and rather requires them to hire a law firm to give them answers to simple questions. This is because popular search engines like Google, and even specialized legal search tools, are either archaic, difficult to use, or fail to provide accurate results from legal search queries.

Our project is to build a web application that enables users to easily search for accurate technical laws, specifically related to capital markets regulations. The product's user interface will be a website with a simple search bar, that will function like a specialized search engine. It will swiftly provide search results of information from 10-K risk factor documents of all S&P500 companies filed with the SEC. This product's goal is to enable semantic search for laws meaning that the user should just be able to input human language without legalese and the correct law will be outputted (something that does not currently exist). We have detailed examples of what different use cases look like in our user stories but at a higher level, this product will be used by law firms, businessmen and law students as an efficient, cheap alternative to search the precise laws surrounding the world of business.

We have included a high-level architecture diagram in our response to Q4 as well as a mockup that can be found in our deliverable-1 folder. 

#### Q2: Who are your target users?

The audience for Lexata’s proposed website is fairly niche. The product’s target users will be those that are required to comply with the legal rules of corporate governance. This includes public companies that are listed on the stock exchange, private companies that are in the process of going public, and law firms. On a user level, Lexata’s website will be most beneficial for individuals who practice law from the financial and investment side of businesses. This largely encompasses legal advisors that work for a company such as in-house legal attorneys, investor relations specialists, and bankers. More specifically, an intended user could be an in-house lawyer responsible for supporting the heads of a company with the legal advice required to make informed and desirable business decisions. 

The following is a user persona:
![user_persona](https://user-images.githubusercontent.com/77204467/152476462-9f61674d-4fb1-45bb-b43e-c1a0c597fdff.png)

#### Q3: Why would your users choose your product? What are they using today to solve their problem/need?

Companies and investment banks will be most interested in Lexata’s services due to its ability to streamline the process of finding capital market regulations in direct and simple language. While Google is an impressive search tool already, it is currently not specialized for legal queries and finding the most relevant and straightforward result from the collection that Google returns can be quite time-consuming and wasteful. On top of this, current specialized legal searching tools are quite outdated and require some knowledge of data science querying techniques that the average law student or attorney would simply not know. To overcome these difficulties, Lexata’s comprehensive database can be queried for correct and relevant legal rules simply through plain language questions. In other words, by removing the abstruse legalese and adopting an easy-to-use searching interface, a user is not required to be an expert to verify compliance rules and those familiar with the law can circumvent the need to learn data querying skills. Lexata’s efficient and straightforward service will allow legal advisors to deliver pertinent legal guidance on securities law matters 55%-75% more expeditiously, freeing up hours of time (that cost $4000 per hour when hiring an expert) for more important matters such as analysis and strategizing. In the long run, Lexata's capabilities for saving time will save a company tens of thousands of dollars in legal consultation fees and will allow individuals to get to what really matters.

#### Q4: How will you build it?

For our technology stack, for the front end specifically, we will be using HTML, CSS, JavaScript and React. We have decided to use mongoDB as the database with MongoDB Compass as a GUI to view and manipulate the data within our database. We chose to use Python, specifically the Django framework, to create the back-end of our webapp. We will be using PyMongo - the official Python driver for MongoDB.

We will use OpenAI (https://beta.openai.com/) - an API that provides access to GPT-3. GPT-3 is a language prediction model that uses deep learning to produce human-like text. OpenAI provides use of GPT-3 for many purposes but we will be using it for its semantic search result capabilities (inputting human language search query and outputting search result taken from database). We will first use OpenAI to create vector embeddings of all of the text documents within our database. This happens once, after collecting all our data. Then, whenever the product is used, OpenAi takes in the search query of the user and returns a vector embedding of that search query. We then use OpenAi to compare this search query embedding to every embedding within the database and rank them by similarities.

Another API we will be using at the beginning of our project is sec-api (https://sec-api.io/profile). We will specifically be using the 10-K Item Extractor API to collect all the data we will need for our database. This API collects data from the U.S Securities and Exchange Commission public company data and we are extracting the “10-K Risk Factors” for all companies in the S&P 500 Index.
For testing, we will creature a test suite with many different search queries that differ from the expected result to varying degrees. Our partner, Leslie, will provide us with the list of expected results since we are unfamiliar with the domain and legalese. 

 There are several deployment options we can choose from, based on the preferences of Lexata’s CEO. Some options include major cloud hosting platforms such as AWS/ Google Cloud/ Microsoft Azure, and there are also several free web hosting platforms we can make use of. The caveat here is that since the final search engine product has a rich database with SEC filing data, and since Lexata intends to use this product as a pitch and selling point for investors, a more reliable, premium web hosting service would be the best option for the company.

Therefore, we will be opting to deploy our web application using Microsoft Azure as the hosting platform. Apart from the fact that Azure is one of the most popular and reliable cloud platforms in the industry, it also has a free tier plan that we can initially utilize to deploy and host our application. Since this service charges on a pay-as-you-grow basis, the application and database can be easily scaled as required by Lexata in the future through premium plans with Azure. The service also has an easy-to-use UI with a plethora of tutorials and help documents to refer to for the deployment phase.

We have created a diagram to visualize the high-level architecture of the product. This demonstrates how the website front-end, back-end, database and OpenAI all interact:

![image](https://user-images.githubusercontent.com/73501632/152447469-975ce4b2-02ab-4365-93b1-598da324465d.png)

#### Q5: What are the user stories that make up the MVP?

Below is the link to the user stories artifacts:
https://docs.google.com/document/d/1-VHujREvgfvzfYRLEhRyNZRd3qNPPYdFEhLS1FnDUwc/edit?usp=sharing


## Intellectual Property Confidentiality Agreement 

We have agreed on option 3 with our partner: "You will only share the code under an open-source license with the partner but agree to not distribute it in any way to any other entity or individual."

## Process Details

#### Q6: What are the roles & responsibilities on the team?

At the beginning of the project, we will have two teams working on different tasks. We will have a group of three working on collecting all
of the data from the SEC website and putting it into a database. The other three teammates will be working on developing the front end of the
website. Since the website is pretty minimal and we have multiple members with experience in web development, we expect that this front end 
will not take very long. The second half of our project will be having a member or two to continue working on the front end, having two members
work with the database and OpenAI and the last two members working on the back end of the website to integrate the database/web interactions.

Here is a detailed table of each team member's responsibilities and skills/difficulties:

<!-- ![image](https://user-images.githubusercontent.com/73501632/152615961-f3db3d98-3350-4a05-923f-9f20bd5e2c14.png) -->

**NAME** | **Roles** | **3 Strengths** | **3 Weaknesses**
-|-|-|-
Sohaib Saqib | Database Scraping, Backend, Deployment, Research web scraping method, Creating meeting agendas | Python development, ORM and Databases, Machine Learning | Front-end development, server-side integration, Django/ Flask
William Wang | Initially Frontend, Backend later on, server API, Research OpenAI API | Python, Web Development (HTML, CSS, JavaScript), C | Databases (SQL), Application deployment, Django framework
Kevin Cecco | Initially Frontend, Backend later on | Web Development (HTML, CSS, JavaScript), Python, Java | Databases, Backend Work, Server Setup and Management
Sepehr Eghbal Yakhdani | Initially Frontend, Backend later on, Research Application Deployment | Web dev (HTML, CSS, JS), Python, Panda/numpy library | Application Deployment, Server Setup, Database and Backend work
Anastasia Young | Database Scraping, Backend, Integration of OpenAi/Database, Research web scraping method, Communication with Partner | Python, Databases, C | Web Development (HTML, CSS, Javascript), Django, Application Deployment
Yijia Zhou | Backend, Database scraping, notetaker during meetings, Research OpenAI API | Python, SQL, working with the Pandas library for databases  | Web Development (HTML, CSS, Javascript), Django, Application Deployment

#### Q7: What operational events will you have as a team?

Meetings will occur weekly with the partner every Wednesday at 8pm EST, over Zoom. In these meetings, we will update the partner on progress
made in that week, address their concerns with the product, and consult them for any related problems which they can be of help to us with.
When we begin the technical work, we will schedule weekly meetings with the subgroup we are working with in addition to the weekly meetings
with the partner. These smaller meetings will be used to plan, divide tasks, do research together, share ideas and also code/debug together. 
The purpose of the meeting will depend on the stage of development we are at at that time. When we approach deadlines, we will also likely 
hold frequent meetings with the entire team online over Zoom, but these would be at our own availability and scheduling.

**Partner Meeting #1 (Sunday January 30th at 2pm EST):**
This meeting was our first introduction to our partner and gave us a basic understanding of the goal of Lexata as well as how the website currently
works. This included exploring the technical aspects of the current MVP provided by the client. From here, we lightly touched upon what our requirements
for the project would be, but from a surface level abstraction. At the end of the meeting, we were able to understand the functionality of the existing
website as well as some of the key tools we would need to use, such as OpenAI.

Meeting Minutes: https://docs.google.com/document/d/1LMkU4QFTP2uDLKc2mRJRbynu_SjKuDBgaaTQGN9hW8o/edit?usp=sharing

**Partner Meeting #2 (Wednesday February 2nd at 8pm EST):**
This meeting covered more about the underlying implementation structure of our app. The partner had asked us to prepare questions about the product
beforehand so we started off by addressing those. By the end of the meeting, we had covered expectations for the backend, frontend, and database, and
also assigned some follow up tasks for the deliverable. The partner also highlighted how some key OpenAI tools are being developed which may be useful
in future modifications to Lexata, but we do not need to focus on these for our project.

Meeting Minutes: https://docs.google.com/document/d/1Mrwq-njx6Ss-idob-2rM_6WipTuwc5SJsfyTWlzPOYk/edit?usp=sharing
  
#### Q8: What artifacts will you use to self-organize?

We will use Monday.com for our To-Do list and task board to keep track of our progress throughout the project. We have 
been using outlook Calendar invites to schedule our weekly meeting with the partner. We collect our meeting notes in a 
single google doc in a table format. We aslo use slack to communicate with each other.
Monday.com helps us keep track of what needs to get done and also helps us determine the status of work (given that it 
has features where you can create customized labels for tasks). This website also has a priority setting so we can rank
tasks by priority. The priority of the task will be determined base on various reasons such as if it is blocking any other
task, if the partner/another team member wants to see the result and then decide future task, the respoinsle person
of the task has other tasks to do etc. 
We will assign tasks to team members as a group. We consider how much work each member has and their skillset for the task 
as well as how much they have contributed recently to the project in assigning tasks.

#### Q9: What are the rules regarding how your team works?

We have been using outlook Calendar invites to schedule our weekly meeting with the partner (Wednesdays 8-9 pm). As for now, we have mainly talked about the project overview and technologies for the website, but as the development starts, we expect to have this meeting to ask questions and clarifications from our partner, reporting the progress of main tasks, decide on task deadlines and starting-dates of new tasks etc. Our communication to our partner happens through a single team member that has already been selected. So far, she has reached out to introduce us to the partner, set up the first couple meetings, follow up after meetings and reach out when we had additional questions. 

We have also decided to use slack as our main in-team communication platform. We use different channels for different sub groups,
asking questions, reporting progress and meeting availibility and we use zoom calls for our meetings. As a group we have agreed on some ground rules such as: Reply to messages daily, check Slack daily, have at least one meeting (other than partner meeting) weekly, communicate with the group if there's a problem, delay or ambiguity regarding your task. (Since we are working in subgroups, one representative would be sufficient for our weekly meeting).

In terms of conflict resolution, although we have set some ground rules to avoid the common problems which can occur during any project, we have set some strategies to resolve them upon occurrence as well. For instance, if a team member is non-responsive, we can designate a single member (which is probably in the same subgroup) to reach out to them personally and ask for the reason. If it’s a personal problem, we will try to distribute their tasks to other team members by adding other team members to their subgroup temporarily and assign some team members to help them as well. But if they are still unresponsive, we will seek help from our TAs and professor. 

Another conflict can be if a team member (or a subgroup) can’t meet the deadline for a task (which can be essential for other tasks). To prevent this, we will have open communication and talk about the deadlines before they are due to get some progress report, then if the deadline looks unachievable we might extend it or in some cases, assign other team members to help them meet that deadline. But if someone consistently can not meet the deadline, they will be talked to personally so we can figure out the problem. It could result in changing the role/task they are working on or adding another team member to the subgroup so the problem can be solved. 

Another scenario could be where a team member is not contributing as much as they should. To address this, we have decided to assign tasks based on how much team members have already contributed or are currently contributing (in that week). So if a team member(or a subgroup) has not done much recently, we will assign more tasks to them in the upcoming week. In addition, we will also be having team bonding experiences to harbour a sense of community that often helps people feel engaged and care more about not letting their teammates down.

A final conflict we considered is if a team member/subgroup has a conflict with our weekly meetings. First of all, since we work in subgroups, one representative from each subgroup would be sufficient for our weekly meetings. But in the case that none of the subgroup members can join the meeting, they must report their progress, questions, 
and problems on the slack channel before the meeting. And if they are unable to do that, we will designate a single member of the group to talk to them and ask for the reason and if it’s possible, change the meeting date and time so at least one person of each subgroup can attend. 


----
## Highlights

Front-end Technology: One of the key decisions in our planning stage was deciding which technologies we would use on our web application. On the front-end, the existing MVP at Lexata uses a WordPress site, written in PHP. One of the downsides to this that was discussed during our meeting was inefficiency (i.e., having to go through WordPress). While the current MVP does not suffer from performance issues, our partner was worried this could become an issue further down the line, when the website will need to search a much more extensive database. One option we considered was keeping the existing UI and attempting to extract out the front-end code to work with our new back-end. The benefit of this approach would be that we could focus more on the back-end search functionality, which is the main focus of the project; the existing front-end already meets the requirements of our partner. The downside would be that a lot of time might be spent attempting to separate the existing front-end with its back-end – time that could have been spent working on a new front-end that would have been designed from the ground up to fit with our project, and would thus be more flexible and adaptive to our features. Furthermore, the existing WordPress site is written in PHP, a language in which we as a team do not have extensive experience. As a result, we as a team decided the best use of our time would be to recreate the page using technologies we are familiar with, including JavaScript and React. 

Back-end Technology: As a team, we agreed to use Python, as it integrates well with the OpenAI model needed for processing searches -- OpenAI has Python libraries that will be useful to us. The exisitng MVP at Lexata also uses Python on the back-end, thus giving us an existing model to work off of when it comes to interfacing with OpenAI. Furthermore, it is a language we are all experienced in and MongoDB, our database technology of choice, works very well with Python.

Database Technology: We chose a non-relational database (specifically MongoDB) over relational for multiple reasons. Our partner requires the original text format of documents stored in the database to be preserved, as well as json line formats. In addition, one of the main objectives of this product is to work with large amounts of data and be very time efficient. All of these requirements point to a non-relational database as being the best database for the task. NoSQL databases are more extendable and are better with storing text documents. As a result, while none of us have experience with MongoDB, we decided to learn this tool as it seems to be the best fit.

The Product: Another decision our team and partner needed to make was to decide which features to include in our initial application. The key functionality of the application involves returning search results (the relevant pieces of legal information stored in our database) based on user input. However, one method we discussed during our meetings was to try to give actual answers to user questions, without legal terms that the typical users of the app may not understand. The benefit of this approach would mostly be for the users – it would give Lexata's application a new feature that could significantly improve the user experience and usefulness of the application. Furthermore, our partner already has ideas for how this could be implemented. However, with this goal in mind, our team decided with our partner that our main focus should be to start with creating a functioning and scalable back-end using a certain category of a legal text (risk factors relating to climate change) to form a foundation for the app, rather than proceeding straight into the special features. A benefit of this approach would be that with an efficient, scalable, and well-designed back-end, the addition of new features such as other areas of law or natural language responses could be easily completed in the future. Without spending enough time on the fundamental functionality, future extensions or modifications could be troublesome and be inefficient. We will implement the extra features if time permits.

Team Responsibilites: Our project requires work on the front-end, back-end, and database. However, in our case, each section of the project may not require the same amount of work. Therefore, when planning our sub-teams, we had a couple of options. On the front-end, the work will be light, as we will be recreating a subset of the existing MVP’s UI. We decided to create a sub-team that has experience with front-end work to get the front-end done relatively quickly. In the meantime, the rest of the team, who have database experience, will work on collecting data to populate the database. Both these tasks will be done in the first part of our project, thus allowing the entire team to concentrate on the back-end, the main bulk of the project. The other alternative would have been to define strict sub-teams, concentrating on only one area of the project. We decided against that since different areas will require varying amounts of work, and will likely be completed at different times (e.g., gathering data to populate the database will need to be done first). Our approach will give everyone the chance to contribute to the main portion of the project throughout the term, thus taking into account every team member’s input. However, we will need to make sure that the same task does not get done twice and no task is left out. We will use our organization artifacts to ensure tasks are distributed properly.


