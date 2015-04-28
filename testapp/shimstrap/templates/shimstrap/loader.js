(function(){
    /* create lookup maps */
    var urlMap = {
        {% for key,value in urlmap %}
        '@{{ key }}':  '{{ value }}',
        {% endfor %}
    };

    /* Cache lookups */


    /* Create the fake server */
    var server = sinon.fakeServer.create();
    var sinon_open = server.xhr.prototype.open;

    server.autoRespond = true;
    server.xhr.useFilters = true;


    server.respondWith("POST", "/echo/html/",
            [200, { "Content-Type": "application/html" }, 'Heyo']);

    server.cache = {};
    server.cache["/echo/html/"] =  0;

    /* Choose when to  */
    server.xhr.addFilter(function(method, url){

        server.cache[url]++;
        if(server.cache[url] == 1)
            return false;
        return true;
    });


    /* Intercept the old xhr open method  */
    server.xhr.prototype.open = function(method, url, a2, a3){
        if(url[0]=='@') url = urlMap[url];
        sinon_open.call(this, method, url, a2, a3);
    };
})();