const getNombre = (idPost) => {
    fetch(`http://jsonplaceholder.typicode.com/posts/${idPost}`)
        .then(res => {
            return res.json()
        })
        .then(post => {
            console.log("Ejemplo Fetch");
            // console.log(post.userId);
            console.log(post.title);
            console.log(post.body);
            fetch(`http://jsonplaceholder.typicode.com/users/${post.userId}`)
                .then(res => {
                    return res.json()
                })
                .then(user => {
                    console.log(user.name);
                    console.log(user.email);
                })
        })
}
// getNombre(12);
getNombre(99);

const getNombreAsync = async(idPost) => {
    try {
        console.log("Ejemplo Async-Await");
        const resPost = await fetch(`http://jsonplaceholder.typicode.com/posts/${idPost}`);
        const post = await resPost.json();
        console.log(post.userId);

        const resUser = await fetch(`http://jsonplaceholder.typicode.com/users/${post.userId}`)
        const user = await resUser.json();
        console.log(user.name);
    } catch (error) {
        console.warn(error);
    }

    // console.log(post.title);
    // console.log(post.body);
}

getNombreAsync(12);

const getNombreAxios = async(idPost) => {
    try {
        console.log("Ejemplo Axios");
        const resPost = await axios(`http://jsonplaceholder.typicode.com/posts/${idPost}`);
        console.log(resPost.data.userId);
        const resUser = await axios(`http://jsonplaceholder.typicode.com/users/${resPost.data.userId}`);
        console.log(resUser.data.name);
    } catch (error) {
        console.log(error);
    }
}

getNombreAxios(12);
