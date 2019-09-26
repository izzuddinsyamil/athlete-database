$(document).ready(function () {
    var athleteId = window.location.pathname.split("/")[2];
    getInitialdata(athleteId);
    getAchievementData(athleteId);

});

function getInitialdata(id) {
    var url = 'http://localhost:8000/api/athlete/' + id;

    $.get(url, function (data, status) {
        if (status == 'success') {
            processSportsData(data["sports"]);
            // processAchievementsData(data["achievements"]);
        } else {
            console.log('failed to get data from ', url);
        }
    });
}

function getAchievementData(id) {
    var url = 'http://localhost:8000/api/achievement-mapping?id=' + id;

    $.get(url, function (data, status) {
        if (status == 'success') {
            processAchievementsData(data["results"]);
        } else {
            console.log('failed to get athlete achievements');
        }
    });
}

function processSportsData(sportList) {
    var sports = '<td>';
    if (sportList.length > 0) {
        sportList.forEach(function (element) {
            sports += element.name + ', ';
        });
        sports = sports.substring(0, sports.length - 2) + '</td>';
    }
    sports += '</td>';
    $('.sports-row').append(sports);
}

function processAchievementsData(achievementList) {
    achievementList.forEach(function (element) {
        result = '<li>';
        result += element.achievement["name"];
        result += ', ' + element.event["name"];
        result += '</li>'
        $('.achievementlist ul').append(result);
    });
}

// function processAchievementsData(achievementList) {
//     var achievements = '<td>';
//     if (achievementList.length > 0) {
//         achievementList.forEach(function (element) {
//             achievements += element.title + ', ';
//         });
//         achievements = achievements.substring(0, achievements.length - 2) + '</td>';
//     }
//     achievements += '</td>';
//     $('.achievements-row').append(achievements);
// }
