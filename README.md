Beebay!

Github repo: https://github.com/LucySargent/crowdfunding/
Deployed app: https://desolate-waters-38107.herokuapp.com/ 

Beebay is a crowdfunding website for 

Baseline features:

Added features:
1. Ability for a beekeeper to 'beefriend' a project
2. Update /delete project
3. Update / delete pledge 
4. Update / delete a beefriend
5. Supburb choice list on project model
6. Number of beehives field on project model
7. Pledge goal property on project model which calculates the funding goal based on number of beehives * the cost of one beehive ($300). 
8. Status property on property model. Shows how much of the pledge goal has been reached. When target has been reached, status shows as "closed".
9. Ability to create, update, delete a user
10. Permissions to ensure !!!

Admin site can be accessed by superuser: https://desolate-waters-38107.herokuapp.com/admin/ 

Get projects
![image](https://user-images.githubusercontent.com/86648895/134754607-d6abe65c-7c1c-49e8-872b-8a37a1c1aaea.png)

Instructions to create a new project:

```json
{
  "title": "This field is required.",
  "description": "This field is required.",
  "suburbs": "This field is required.",
  "beehives": "This field is required.", 
  "image": "This field is required.",
  "is_open": "This field is required.",
  "date_created": "This field is required."
}
![image](https://user-images.githubusercontent.com/86648895/134755452-530fd62d-e456-47fa-bd45-13efeca53b2d.png)


![image](https://user-images.githubusercontent.com/86648895/134754724-dfaf19c0-6494-4141-95a0-cdae08026d13.png)
