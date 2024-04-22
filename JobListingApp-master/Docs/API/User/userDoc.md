#   User End Points

### Available Actions

-   Create User
    - url : /api/user/create
    - method : POST
    - body : name,email,password
    - returns : username & email
    
-   Get Authentication Token 
    - url : /api/user/token
    - method : GET
    - body : email, password
    - return : "userAuthToken"
 
-   Get User Profile <@AuthenticatedRoute>
    - url : api/user/profile
    - method: GET
    - body: none
    - Headers : Authorization : Token "userAuthToken"
    - returns : username & email
    
    
     