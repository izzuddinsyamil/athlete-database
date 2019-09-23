$(document).ready(function () {
    GetInitialData();

    $(".sort-age").hover(function () {
        $(this).css("cursor", "pointer");
    });

    $(".sort-name").hover(function () {
        $(this).css("cursor", "pointer");
    });

    ageSortedBy = "-age/";
    $(".sort-age").click(function () {
        $("#athlete-table").find("td").remove();

        var url = "api/athlete/sort/" + ageSortedBy;
        $.get(url, function (data, status) {
            if (status == 'success') {
                if (ageSortedBy == 'age/') {
                    ageSortedBy = "-age/"
                } else {
                    ageSortedBy = "age/"
                }

                data["results"].forEach(function (element) {
                    ProcessAthleteData(element);
                });
            } else {
                console.log('failed to get data from ', url);
            }
        });
    });

    nameSortedBy = "-name/";
    $(".sort-name").click(function () {
        $("#athlete-table").find("td").remove();

        var url = "api/athlete/sort/" + nameSortedBy;
        $.get(url, function (data, status) {
            if (status == 'success') {
                if (nameSortedBy == 'name/') {
                    nameSortedBy = "-name/"
                } else {
                    nameSortedBy = "name/"
                }

                data["results"].forEach(function (element) {
                    ProcessAthleteData(element);
                });
            }
        });
    });
});

function GetInitialData() {
    var url = "api/athlete/";
    $.get(url, function (data, status) {
        if (status == 'success') {
            data["results"].forEach(function (element) {
                ProcessAthleteData(element);
            });
        }
    });
}

function ProcessAthleteData(json) {
    var resp = '<tr class="athlete-row">' +
        '<td scope="row">' + '<a href="atlet/' + json["id"] + '">' + json["name"] + '</a></td>' +
        '<td>' + json["age"] + '</td>' +
        '<td>' + json["birth_date"] + '</td>' +
        '<td>' + json["address"] + '</td>'
        ;

    resp += parseSportsListToHtml(json['sports']);

    resp += parseAchievementListToHtml(json["achievements"]);
    resp += '</tr>';

    $('.athlete-data').append(resp);
}

function parseSportsListToHtml(sportList) {
    var sports = '';
    if (sportList.length > 0) {
        sports += '<td>';
        sportList.forEach(function (element) {
            sports += element.name + ', ';
        });
        sports = sports.substring(0, sports.length - 2) + '</td>';
    }
    return sports
}

function parseAchievementListToHtml(achievementList) {
    var achievements = '';
    if (achievementList.length > 0) {
        achievements += '<td>';
        achievementList.forEach(function (element) {
            achievements += '<a href="prestasi/' + element.id + '">' + element.title + '</a>, ';
        });
        achievements = achievements.substring(0, achievements.length - 2) + '</td>';
    }
    return achievements;
}