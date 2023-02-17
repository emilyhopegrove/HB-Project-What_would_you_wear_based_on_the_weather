//add event listener to form x
//document.queryselector using id x
//add event listener for submitting args->(event we listen form, some action)
//give that a callback function



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