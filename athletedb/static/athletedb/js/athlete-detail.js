$(document).ready(function () {
    getInitialdata();
});

function getInitialdata() {
    var url = 'http://localhost:8000/api/athlete/' +
        window.location.pathname.split("/")[2];

    $.get(url, function (data, status) {
        if (status == 'success') {
            processSportsData(data["sports"]);
            processAchievementsData(data["achievements"]);
        } else {
            console.log('failed to get data from ', url);
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
    var achievements = '<td>';
    if (achievementList.length > 0) {
        achievementList.forEach(function (element) {
            achievements += element.title + ', ';
        });
        achievements = achievements.substring(0, achievements.length - 2) + '</td>';
    }
    achievements += '</td>';
    $('.achievements-row').append(achievements);
}
