###Blogger API

Please refer to deployment and configuration section for deployment instructions.

This documentation is intended for the developers who wants to integrate with this blogger API. All APIs are REST compliant, strictly follow HTTP. On success return HTTP 200 OK.

#### Important concepts
Users: Users are either the logged in user(s) or just readonly public user.
Blogs, signed in users create blog(s), and they can make post(s) to their blog(s). Signed in user(s) can make posts to other blog(s), created by other user(s). 

#### Table of Contents
[TOC]

####User Management APIs

##### GET /users/register
Description: Registers a new user.

Input:
	-	user_id: Unique user id
	-	password: Passowrd for the user

Response:
	-	HTTP 200 OK on Sucess

##### GET /users/login
Description: Login a user with a valid user_id and password.

Input:
	-	user_id: User ID
	-	password: Password

 RETURNS:
	-	A user session cookie (HTTP Session).
	-	 Session has a TTL

##### GET /users/logout
Desrciption: Logout a user, deletes the session.

#### Blog and Posts Access Control

##### GET /blogs/blogId/access

Desrciption: Current logged in user requests for access to a certain blog

##### GET /blogs/manage

Desrciption: List of requests for 'permissions' by other users.

##### GET /blogs/requestId/approve

Desrciption: Approve an access requests.

#### Blogs and Posts

##### GET /blogs/blogId

Desrciption: Get a blog by ID


##### GET /blogs/users/userId?start_page=0&pages=1

Get blogs of a user UserId

    start_page: Optional 'page' id (if user has multiple page full of blogs)
	pages: Numbver of pages 

##### POST /blogs/blogId

Adds a blog for a user.


 ##### GET /blogs/blogId/posts
Posts from a BLOG

 ##### GET /blogs/blogId/posts/postId
A specific post

##### POST /blogs/blogId/posts/
Add a POST to a blog

##### DELETE /blogs/blogId/posts/postId
DELETE a POST

##### PUT /blogger/v3/blogs/blogId/posts/postId
Update a POST

#### Deployments and Configuration



