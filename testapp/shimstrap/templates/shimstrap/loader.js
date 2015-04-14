(function(){
    var map = {
        {% for key,value in urlmap %}
        '{{ key }}':  '{{ value }}',
        {% endfor %}
    };

    window.__urlmap = map;
})();