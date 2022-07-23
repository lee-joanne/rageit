# Rageit

[View live project here](https://rageit.herokuapp.com/)

## User Experience (UX)

### User Stories

- Users: 

    1. As a **user** I can **view posts on the main page with the excerpt** so that **I can quickly read which post seems interesting to me before clicking on it and reading further.**

    2. As a **user** I can **sign up easily with just a username and password** so that **I have the ability to create posts or comments without having to share my email address.**

    3. As a **user** I can **create posts** so that **I can share my own rage-worthy posts.**

    4. As a **user** I can **share photos in my posts** so that **I can add photographic evidence or add context to my rage-worthy posts.**

    5. As a **user** I can **make comments on posts** so that **I can share my thoughts on other people's rage-worthy posts.**

    6. As a **user** I can **revise my posts** so that **I can make any changes if needed.**

    7. As a **user** I can **delete my posts** so that **I have the freedom to remove any posts I no longer want to be shared.**

    8. As a **user** I can **delete my comments** so that **I have the freedom to remove any comments I no longer want to be shown.**

    9. As a **user** I can **easily log out** so that **I can have more security on my account.**

    10. As a **user** I can **easily log in** so that **I can quickly post or add more comments if I wish.**

    11. As a **user** I can **easily see how many posts or comments each post has in the homepage** so that **I can see which posts are popular or have the most comments if I wanted to read the most popular posts.**

    12. As a **user** I can **only edit and delete my own posts and view an error message if I tamper with the URL to edit or delete someone else's post** so that **I can have enhanced security and ensure no one tampers with my posts.**

    13. As a **user** I can **receive feedback immediately if I have uploaded an incorrect file or image type** so that **I can immediately know to fix my file or image before submitting a new or edited post or comment.**

    14. As a **User** I can **like posts or click again to unlike** so that **I can show my appreciation towards a post by liking, or change my mind and dislike later.**


- Site Admin: 

    1. As a **site admin** I can **review, create, and delete posts** so that **I can manage my website's main layout and content.**

    2. As a **site admin** I can **review, create, and delete comments on posts** so that **I can manage the comments and content on posts.**

### Data Model

- Data model has been created using the program Whimsical
- ![Screenshot of Data Model](documentation/datamodel.png)

### Wireframes

- Wireframes have been created using the program Whimsical

    - Mobile: 
        ![Screenshot of Mobile Wireframe](documentation/wireframes/mobile_wireframe.png)

    - Tablet: 
        ![Screenshot of Tablet Wireframe](documentation/wireframes/tablet_wireframe.png)

    - Desktop:
        ![Screenshot of Desktop Wireframe](documentation/wireframes/desktop_wireframe.png)

## Features

### Existing Features

## Technologies Used

### Languages and Python Packages/Libraries Used

### Frameworks, Libraries & Programs Used

1. [Git](https://git-scm.com/)
    - Git was used by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

2. [GitHub](https://github.com/)
    - GitHub was used to store the project code after being pushed in by Git. Project repository linked with Heroku for deployment process. 

3. [Heroku](https://dashboard.heroku.com/login)
    - Heroku was used to deploy the Python project as a terminal based game after signing in with GitHub. 

4. [Whimsical](https://whimsical.com)
    - Whimsical was used to create the flowchart for the game. 

5. [PEP8 Online Check](http://pep8online.com/)
    - PEP8 Online Check was used to validate the Python code used and check for warnings/errors. 

6.  [Ecotrust-Canada Markdown-toc](https://ecotrust-canada.github.io/markdown-toc/)
    - Ecotrust-Canada Markdown was used to create the table of contents for this README. 

## Testing

### Bugs

## Deployment

- The following steps were taken for the deployment process:

    1. Ensure that the template used for the project is made with the Code Institute Python template linked above. 
    2. Second, in all Python scripts, ensure that input methods have a new line character at the end of the text inside.
    3. If any packages or installments were made, type in the following command in the terminal: **'pip3 freeze > requirements.txt'** so these installments / dependencies can work on Heroku. After typing this in, the requirements.txt file in the Code Institute Python template will automatically be updated. 
    4. Commit and push these changes onto GitHub.
    5. [Create an account for Heroku](https://id.heroku.com/login)
    6. On the Heroku dashboard, go to **Create new app**. 
    7. Name your app (must be a unique name) and select your region, and go to **Create app**.
    8. On the next page after selecting **Create app**, go to the **Settings** tab. Scroll down to **Config Vars** and select **Reveal Config Vars**.
    9. Since no APIs or Creds were used for Pirate Ship, the only Config Vars added was:
    Key: PORT / 
    Value: 8000
    10. Next, scroll down to **Buildpacks**. Click **Add Buildpack** and select **Python** and **Save Changes**. Next, add **nodejs** and **Save changes**. Ensure Python is on top and nodejs is below. 
    11. Next, scroll up and go to the **Deploy** tab.
    12. Under **Deployment method**, select **GitHub** and confirm **Connect to GitHub**. 
    13. Search for your repository name and click **Connect**.
    14. Scroll down and select **Deploy Branch** next to **Manual Deploy**. Ensure the branch to deploy is master/main. 
    15. Deployment gets created and live link is then previewed. 

[View live project here](https://pirate-ship54.herokuapp.com/)

## Credits

### Code

### Acknowledgements













