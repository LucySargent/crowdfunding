**BEEBAY!** 

Beebay is a crowdfunding website linking potential beehive locations, beekeepers and community sponsors to increase the number of bees in Queensland.

Github repo: https://github.com/LucySargent/crowdfunding/

Deployed app: https://desolate-waters-38107.herokuapp.com/ 

Admin site can be accessed by superuser: https://desolate-waters-38107.herokuapp.com/admin/


**MVP features:** 
1. Ability to create a user account
2. User can create a project to be funded
3. User can “pledge” to a project
4. Suitable update/delete functionality 
5. Suitable permissions
6. Return the relevant status codes for both successful and unsuccessful requests to the API
7. Handle failed requests gracefully
8. Use Token Authentication 


**Added features:**
1. Ability for a user to 'beefriend' a project
2. 'Suburb' choice list added to project model
3. 'Number of beehives' field added to project model
4. 'Pledge goal' property added to project model. Calculates the funding goal based on number of beehives * the cost of one beehive ($300). 
5. 'Status' property added to property model. Shows how much of the pledge goal has been reached. When target has been reached, status shows as "closed".
6. Limited pledge list view to superuser only

**Added permissions**





Get all projects:
![image](https://user-images.githubusercontent.com/86648895/134754607-d6abe65c-7c1c-49e8-872b-8a37a1c1aaea.png)


Get individual project:


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
