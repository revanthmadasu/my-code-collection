// promises experimentation
const serviceableResObj = {
    data: {
        is_address_serviceable: true,
        deliveryDetails: {
            deliveryPartner: {
                name: "Revanth",
                contact: "9347588320"
            }
        }
    }
};

const unServiceableResObj = {
    data: {
        is_address_serviceable: false
    }
};

const apiCall = (isServiceable) => new Promise((res, rej) => {
    setTimeout(() => {
        if (isServiceable === true) {
            res(serviceableResObj)
        } else if (isServiceable === false) {
            res(unServiceableResObj);
        } else {
            rej({
                statusCode: 400,
                error: "Data not provided in request. Try making request with data"
            });
        }
    }, 500);
});

function makeApiCall(requestData) {
    return apiCall(requestData).then(resData => {
        // console.log(resData);
        if (resData && resData.data && resData.data.is_address_serviceable) {
            return Promise.resolve(resData.data.deliveryDetails)
        } else {
            // console.log("rejecting promise");
            return Promise.reject("Delivery not possible to selected location");
        }
    }).catch(error => {
        // console.log("receiver error from api: ");
        // console.log(error);
        // console.error(`Request unsuccessful. Message: ${error.error}`);
        return Promise.reject(error);
    });
}

function makeServiceCall(requestData) {
    makeApiCall(requestData).then((data) => {
        // console.log(`Recieved data from service is ${data}`);
        console.log(`Ordered successfully. Your delivery partner is ${data.deliveryPartner.name}`);
    }).catch(error => {
        console.error(`Your order is unsuccessful. ${error}`);
    });
}

makeServiceCall(true);
makeServiceCall(false);
makeServiceCall();