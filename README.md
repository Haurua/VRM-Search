# VRM-Search

A web-application showing the basic information of a UK registered vehicle by searching it's VRM (vehicle registration mark). It offers the same information as the official gov.uk website.

The information provided is retrieved directly from DVLA using their API key. The response is converted to JSON format which is then parsed and displayed in the template.

This application was built to take advantage of the API key that the DVLA kindly provided. A separate function was created to handle the API request, which is called by the view when a number plate is submitted.

If the response status code is 200, the results are then displayed. Otherwise, an error message is passed in to the HTTP response to inform the user when redirected.

# In-Depth Details

I wanted to call my own functions as part of the view to achieve a specific task. I secured an API key from the DVLA which allowed me to access to their database.

I used two libraries to achieve the functionality of this web-application; requests and datetime. The dvla_api_request function assembles the payload, makes a request and returns the response.

Some data provided by the response is not visually appealing, such as the date: '2022, 03, 12'. With this in mind, I created custom tags that would format the date to '03 March, 2022' using the datetime library.

This helped me to better understand classes since I was dealing with datetime objects, and importance of inheritance, especially when adhering to DRY principles.

As for the visual design, it borrows heavily from the DVLA website. I wanted to replicate their design to test my HTML/CSS skill by turning design in to code. I did not refer to their actual code during the design phase.

I wanted to use a little media queries as possible, so only one query is used for modifying the padding, the rest of the application is responsive using the CSS Grid system.
