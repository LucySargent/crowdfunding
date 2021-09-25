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


**Added permissions**
Added restrictions to get/post/put/delete methods. This is work in progress - some are not logical and need changing!

![image](https://user-images.githubusercontent.com/86648895/134766847-25528412-680e-4b56-ac02-6350eb4c0d49.png)

![image](https://user-images.githubusercontent.com/86648895/134766865-2a764ba1-8b66-40d3-9ac9-7140a4092f9b.png)

![image](https://user-images.githubusercontent.com/86648895/134766875-8644eb57-b5f0-43f9-87e7-10275778b1bd.png)

![image](https://user-images.githubusercontent.com/86648895/134766902-608a29b0-d0f1-4d03-bbfd-82517898423d.png)


Get all projects:
![image](https://user-images.githubusercontent.com/86648895/134754607-d6abe65c-7c1c-49e8-872b-8a37a1c1aaea.png)


Request body to create a new project:

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
```

![image](https://user-images.githubusercontent.com/86648895/134755452-530fd62d-e456-47fa-bd45-13efeca53b2d.png)
