$(document).ready(function () {
    var athleteId = window.location.pathname.split("/")[2];
    getInitialdata(athleteId);
});

function getInitialdata(id) {
    var url = '/api/athlete/' + id;

    $.get(url, function (data, status) {
        if (status == 'success') {
            processAthleteBio(data);
            processSportsData(data["sports"]);
            processAchievementData(data["achievements"]);
        } else {
            console.log('failed to get data from ', url);
        }
    });
}

function processAthleteBio(athleteData) {
    var birthDateAndAge = athleteData.birth_date + ` (` + athleteData.age + ` tahun)`;

    $("#athlete-name").text(athleteData.name);
    $("#athlete-nik").text(athleteData.nik);
    $("#athlete-birthdate").text(birthDateAndAge);
    $("#athlete-birthplace").text(athleteData.birth_place);
    $("#athlete-sex").text(athleteData.name);
    $("#athlete-bloodtype").text(athleteData.blood_type);
    $("#athlete-phone").text(athleteData.phone_number);
    $("#athlete-address").text(athleteData.address);
    $("#athlete-email").text(athleteData.email);
    $("#athlete-school").text(athleteData.school);
} 

function processSportsData(sportList) {
    var sports = '';
    if (sportList.length > 0) {
        sportList.forEach(function (element) {
            sports += element.name + ', ';
        });
        sports = sports.substring(0, sports.length - 2);
    }

    var sportData = `
    <dd class="col-sm-9">` + sports + `</dd>`;
    $('.athlete-bio-detail').append(sportData);

}

function processAchievementData(achievementList) {
    achievementList.forEach(function (element) {
        var achievementID = `achievement-` + element.id;
        var achievementTitle = element.result + `, ` + element.level;

        var certificateImg = `<p class="font-italic">Tidak ada file sertifikat</p>`;
        if (element.certificate_file != null) {
            certificateImg = `<img src="` + element.certificate_file + `" class="achievement-img" width="500" height="300"></img>`
        }

        var achievementData = `
        <div class="achievement-per-athlete shadow-sm p-4 mb-4 bg-white rounded" id="` + achievementID + `">
            <div class="achievement-title border-bottom mb-3">
                <h5>`+ achievementTitle + `</h5>
            </div>
            <div class="achievement-body">
                <div class="achievement-desc mt-1 mb-3">` + element.description + `</div>
                <div class="achievement-certificate mb-3">
                    sertifikat : <br>
                    ` + certificateImg + `
                </div>
            </div>
        </div>
        `;

        $(".achievement-list").append($(achievementData));
    });
}