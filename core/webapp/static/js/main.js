
async function makeRequest(url, method='GET'){
    let response = await fetch(url, {method});

    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }

}

function onError(error) {
    console.log(error);
}


async function addLike(event){
    event.preventDefault();
    let target = event.target;
    let url = target.href;
    try {
        let response = await makeRequest(url);
        console.log(response);
        let articleId = target.dataset.articleId;
        let text = document.getElementById(articleId);
        checkText(text);
        let count = response.count;
        let p = document.getElementById('total_likes');
        p.innerText = `Total likes ${count}`;
    }
    catch (error){
        onError(error);
    }
}

async function addLikeComment(event){
    event.preventDefault();
    let target = event.target;
    let url = target.href;
    try {
        let response = await makeRequest(url);
        console.log(response);
        let commentId= target.dataset.commentId;
        let text = document.getElementById(commentId);
        checkText(text);
    }
    catch (error){
        onError(error);
    }
}

function checkText(text){
    if(text.innerText === "Dislike"){
            text.innerText = "Like";
        } else {
            text.innerText = "Dislike";
        };
    return text;
}

async function onloadFunc() {
    let likes = document.getElementsByClassName("likes");
    for (let i = 0; i < likes.length; i++) {
        likes[i].addEventListener("click", addLike);
    }
    let favourites = document.getElementsByClassName('favourites');
    for (let j = 0; j < favourites.length; j++) {
        favourites[j].addEventListener("click", addLikeComment);
    }
}

window.addEventListener("load", onloadFunc);