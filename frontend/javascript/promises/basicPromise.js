function asyncOperation() {
    console.log("started executing");
    return new Promise(res => {
        setTimeout(() => res(), 500);
    });
}

asyncOperation().then(() => {
    console.log("done executing");
});