function pagination(page) {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        const result = JSON.parse(xhttp.responseText);
        var html = "";
        var recipes = result["result"]["recipes"];
        console.log(result);

        for (var recipe in recipes) {
            console.log(recipes[recipe]['id'])
            html += "<a href='/rango/recipe/" + recipes[recipe]['id'] + "'>\n<li><img src='" + recipes[recipe]['url'] + "' alt='dish' /><p>" + recipes[recipe]['name'] + "</p></li>\n</a>"
        }
        document.getElementById("recipe-list").innerHTML = html;

        html = "";
        var page_obj = result['result']['page_obj'];
        console.log(page_obj)
        if (page_obj['has_prev']) {
            html += "<li><a onclick='pagination(1)'>&laquo;</a></li>\n";
            html += "<li><a onclick='pagination(" + page_obj['prev_num'] + ")'>" + page_obj['prev_num'] + "</a></li>\n";
        }
        html += " <li><a class='active'>" + page_obj['num'] + "</a></li>\n";
        if (page_obj['has_next']) {
            html += "<li><a onclick='pagination(" + page_obj['next_num'] + ")'>" + page_obj['next_num'] + "</a></li>\n";
            html += "<li><a onclick='pagination(" + page_obj['num_pages'] + ")'>&raquo;</a></li>\n";
        }
        document.getElementById("page-numbers").innerHTML=html;
        //console.log(xhttp.responseText);
    }
    xhttp.open("GET", "pagination/?page=" + page);
    xhttp.send();
}