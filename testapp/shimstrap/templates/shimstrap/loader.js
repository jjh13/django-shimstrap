(function(){
    /* create lookup maps */
    var urlMap = {};

    /****
    * '@url -> {hashofparams: data}
    */

    /* Create the fake server */
    var server = sinon.fakeServer.create();
    var sinon_open = server.xhr.prototype.open;

    server.autoRespond = true;
    server.xhr.useFilters = true;

    server.respondWith("POST", "/echo/html/",
            [200, { "Content-Type": "application/html" }, 'Heyo']);

    server.cache = {};
    server.cache["/echo/html/"] =  0;

    /* Choose when to load from server  */
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

    /* Cache lookups */
    var elements = document.getElementsByClassName("_dss_preload");
    for(var i=0; i < elements.length; i++) {
        var id = elements[i].id.split(':');
        var cached_data = JSON.parse(elements[i].innerText);
        var hashkey = id[0];
        var urlhash = "@" + id[1];
        var url = id[2];
        var method = id[3];

        urlMap[urlhash] = urlMap[urlhash] || {};
        urlMap[urlhash][hashkey] = cached_data;
    }

    // Wonderful, we don't need to export anything once this has run.
    return;
})();