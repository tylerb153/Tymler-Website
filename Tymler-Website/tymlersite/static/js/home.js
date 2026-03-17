const url = "https://api.mcstatus.io/v2/status/java/mc.theminecraftcult.com"

document.addEventListener('DOMContentLoaded', getStatus())
setInterval(getStatus, 30000);

function getStatus() {
    fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network Error');
        }
        return response.json();
    })
    .then(data => {
        setInfoPanelDetails(data)
    })
    .catch(error => {
        console.error('Error: ', error);
    });
}

function copyServerAddress(element) {
    navigator.clipboard.writeText("mc.theminecraftcult.com");

    element.innerText = "Copied!";
    
    setTimeout((element) => {element.innerText = "mc.theminecraftcult.com";}, 2000, element)
}


function setInfoPanelDetails(data) {
    // console.log(data)
    const statusElement = document.getElementById('serverStatus');
    const versionElement = document.getElementById('version-label');
    const playersListElement = document.getElementById('serverPlayersList');
    const playersLabel = document.getElementById('serverPlayersLabel');

    if (data.online) {
        statusElement.classList.remove('text-danger');
        statusElement.classList.add('text-success');
        statusElement.innerText = "Online";
        versionElement.innerText = `Version: ${data.version.name_clean}`;
        playersLabel.innerText = `${data.players.online}/${data.players.max} Players`

        var playersListHTML = "";
        for (player of data.players.list) {
            playersListHTML += `<li><i class="bi bi-person-fill me-1"></i>${player.name_clean}</li>`;
        }
        playersListElement.innerHTML = playersListHTML;

    } else if (!data.online) {
        statusElement.classList.remove('text-success');
        statusElement.classList.add('text-danger');
        statusElement.innerText = "Offline";
        versionElement.innerText = "";
        playersListElement.innerHTML = "";
        playersLabel.innerText = "";
    }
}