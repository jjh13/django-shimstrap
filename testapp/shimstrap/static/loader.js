(function(){
    /* create lookup maps */
    var urlMap = {};

    /* Create the fake server */
    var server = sinon.fakeServer.create();
    var sinon_open = server.xhr.prototype.open;

    server.autoRespond = true;
    server.xhr.useFilters = true;

    /* Choose when to load from server  */
    server.xhr.addFilter(function(method, url){
        if(urlMap[url]){
            urlMap[url] = false;
            return false;
        }
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
        var element = elements[i];
        var method = element.getAttribute('data-method');
        var url = element.getAttribute('data-url');
        var type = element.getAttribute('data-type');
        var cached_data = element.innerText;
        var hash_id = element.id;

        urlMap[url] = true;
        server.respondWith(method, url,  [200, { "Content-Type": type}, cached_data]);

        // Cleanup the dom
        document.getElementById(hash_id).remove();
    }

    // Wonderful, we don't need to export anything once this has run.
    return;
})();