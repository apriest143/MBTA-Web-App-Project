Andrew Priest, Cole Davenport | Assignment 3 | OIM 3640

**1. Project Overview** (~1 paragraph)

Write a short abstract describing your project. Summarize the main objectives, key features, and any extensions or additional functionality implemented beyond the basic requirements.

This project completes a very specific function. It presents a web app to a user and prompts them to input a location. This location is then pushed to the next page of the website using the POST method where it is ran through a python program working in tandem with the MBTA API. This program returns both the nearest MBTA stop (Calculated using longitude and latitude), and whether that stop is handicap acessible. This information is then presented on the web app, and the user is prompted to input another location.

**2. Reflection** (~3 paragraphs + screenshots)

After you finish the project, Please write a short document for reflection.

- Discuss the **development process** point of view, including what went well and what could be improved. Reflect on topics such as project scoping, testing, debugging, and any specific challenges encountered. What strategies helped the team succeed, and what adjustments might have made the project smoother?

The development process of this project was not exactly smooth. We had gotten a late start initially, and quickly fell behind schedule. This ended up making the rest of the process more difficult as any difficulties we faced were made worse due to the time constraint we were working under. We then both got hit with a lot of work from other classes which made it much harder to coordinate time and work together. We scoped our project well, but really struggled on making significant strides as issues would quickly compound and slow down our progress. Starting earlier and having consistent times to meet would be a great way to avoid these issues goinf forward. We will work on being more consistent going forward.

- Discuss your **team's work division**, including how the work was planned to be divided and how it actually happened. Address any issues that arose while working together and how they were addressed. Finally, discuss what you would do differently next time.

Our team divided the work quite evenly. Cole focused primarily on the API while Andrew worked with the flask and helped debug. The API was certainly the more complex aspect of this project, so we prioritized in person coding to ensre that both team members were seeing the code evolve. We were having some issues with the program, namely it returning one location regardless of input, but through debugging we were able to understand the why it was miscalculating the longitude and latitude fields and giving us the error. Our best work was done in person for this assignment, and that is something we will prioritize going forward.

- Discuss from a **learning** perspective, what you learned through this project and how you'll use what you learned going forward. Share your experience with AI tools - did they enhance your efficiency or understanding, and if so, how? What do you wish you had known beforehand that would have helped you succeed? Include screenshots showing key stages of development or specific challenges you overcame.

This project was a great exercise in implementing real world functionality from API's and connecting them to the web design techniques we have learned in class. This is incredibly applicable for our term project as we must leverage APIs in order to build out the functionality of our program and apply it in the real world with a web app.
In terms of AI usage it was incredibly helpful with brainstorming some of the potential issues that we ran into when trying to access the API. PUT SCREENSHOT HERE COLE
It also was very helpful with explaining the concept of the template and how it works in tandem with the rest of the program to deliver its value as this was an aspect of the project we had minimal experience working with.(Albiet in a very long winded way)
![alt text](<Screenshot 2024-11-12 171918.png>)