function analyzeGuess(json_response) {
    var play_status = document.getElementById("play_status")
    var outcome = json_response.outcome;
    var game = json_response.game;
    var analysis = outcome.analysis;
    var status = game.status;
    var cows = outcome.cows;
    var bulls = outcome.bulls;

    if (status == "won" || status == "lost") {
        play_status.innerHTML = outcome.message;
        if (analysis == undefined || analysis == '') {
            return;
        }
    } else {
        play_status.innerHTML = "You have " + bulls + " bull(s) and " + cows + " cow(s).";
    }

    for (var i = 0; i < g_digits; i++) {
        var outfield = document.getElementById('row_' + (g_try - 1)  + '_col_'+i);
        outfield.innerHTML = analysis[i].digit;
        outfield.className = "nothing";
        console.log('Checking match --> ' + analysis[i].match);
        console.log('Checking in_word --> ' + analysis[i].in_word);
        console.log('Checking multiple --> ' + analysis[i].multiple);
        if (analysis[i].in_word) {outfield.className = "cow "}
        if (analysis[i].match) {outfield.className = "bull "}
        if (analysis[i].multiple) {outfield.className += " multiple "}
    }
/*    alert(json_response.outcome.bulls + ' bulls and ' + json_response.outcome.cows + ' cows.'); */
}

function parseToJSON(text) {
    var jsonResponse = {};
    try {
        jsonResponse = JSON.parse(' ' + text + ' ');
    }
    catch(err) {
        console.log('Error: ' + err);
        console.log('Input text was: ' + text);
    }
    return jsonResponse;
}

function parseResponse(text) {
    var start=text.indexOf("{")
    var end=text.indexOf("}") + 1
    return text.substring(start, end)
}

function makeGuess() {
    var play_status = document.getElementById("play_status");
    play_status.innerHTML = "Connecting to game server. Please wait...";

    /* Build digits */
    list_of_guesses = [];
    for (var dig = 0; dig < g_digits; dig++) {
        digit = document.getElementById('digit_'+dig);
        list_of_guesses.push(parseInt(digit.value));
    }
    params = {
        key: g_key,
        digits: list_of_guesses
    }

    /* Make a guess */
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        var json_response = {};

        if (this.readyState == 4) {
            if (this.status == 200) {
                g_try++;
                console.log('Success. Processing game response ' + this.responseText);
                json_response = parseToJSON(this.responseText);
                analyzeGuess(json_response);
            } else {
                console.log('An error occurred: ' + this.responseText);
            }
        }
    };

    xhttp.open("PUT", '/', true)
    xhttp.setRequestHeader("Content-Type", "application/json")
    xhttp.send(JSON.stringify(params), "json")
}