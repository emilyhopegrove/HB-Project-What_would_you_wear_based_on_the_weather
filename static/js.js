//add event listener to form x
//document.queryselector using id x
//add event listener for submitting args->(event we listen form, some action)
//give that a callback function

//User account details update form
    //let user know their details have been updated and add an event listener to the account update form button
    //reset the form without refreshing the form using AJAX
function accountDetailsUpdate(results){
    if(results.message === 'Account details updated!'){
        //the message below is not showing up (the garments message is)
        alert('Success! Your account details have been updated and added to our database')
        document.getElementById('account-details').reset();
    }
}

function accountDetailsUpdater(evt){
    evt.preventDefault();
    const formInputs = {
        email: document.querySelector('#email').value,
        username: document.querySelector('#username').value,
        homeZip: document.querySelector('#homeZip').value,
        workZip: document.querySelector('#workZip').value,
        otherZip: document.querySelector('#otherZip').value,
    };
    fetch('/accountDetailsUpdater', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
            'Content-Type': 'application/json',
        },
    })
    .then((response) => response.json())
    .then(accountDetailsUpdate);

}
//probably need to make a different button for this to listen for...
document.querySelector('#account-details').addEventListener('submit', accountDetailsUpdater);

//Garment adder form
function garmentUpdates(results){
    if(results.message === 'Garment added!'){
        alert('Success! Garment has been added to our database')
        document.getElementById('add-garment').reset();
}


}

function garmentAdder(evt){
    evt.preventDefault();
    const formInputs = {
        garment_type: document.querySelector('#garment-type').value,
        garment_description: document.querySelector('#garment-description').value,
        temperature_rating: document.querySelector('#temperature-rating').value
    };
    fetch('/usersGarments', {
        method: 'POST',
        body: JSON.stringify(formInputs),
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then((response) => response.json())
      .then(garmentUpdates);

}

document.querySelector('#add-garment').addEventListener('submit', garmentAdder);