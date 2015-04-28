# django-shimstrap

Shimstrap is a small Django extension that aims to rectify two problems when dealing with AJAX based application in
Django. Firstly, it provides a mechanism for distinguishing AJAX calls from non-AJAX calls in the URL router via
`ajax_url`. This allows you to register a URL to a service name. Once you've included the necessary accompanying
JavaScript, you can make AJAX calls directly to those registered names. For example, you may register
`get_user_posts` to the URL `/user/get-posts/`, then simply do an AJAX call to `@get_user_posts` with your favourite
front end library.

Shimstrap also provides mechanisms for caching 'first-loads' for JSON data. For example, we can associate the
the dictionary `{post:"my cool data"}` with the name `get_user_posts` via
``preload_ajax(request, 'get_user_posts', {"post":"my cool data"})``
The first time any ajax call to '@get_user_posts' happens within the page, `{"post":"my cool data"}` will be returned
without hitting the server.

Currently all this functionality is provided by Sinon.js, which provides us with a fake XMLHttpRequest object that
can be customized to our liking. This is a nice first step, but we should consider rolling our own solution, as that
library includes many things we don't need, and licensing issues may get tricky.

