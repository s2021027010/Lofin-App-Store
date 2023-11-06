

 
 /*
 // Create an instance of the Stripe object with your publishable API key

 var checkoutButton = document.getElementById('checkout-button');
 var id = document.getElementById('db_id_App');
 var AppName = document.getElementById('db_AppName');
 var price = document.getElementById('db_price');

 checkoutButton.addEventListener('click', function() {
 // Create a new Checkout Session using the server-side endpoint you
 // created in step 3.
 fetch('/create-checkout-session/' + id +"/" + AppName + "/" + price, {
 method: 'POST',
 
 })
 .then(function(response) {
 return response.json();
 })
 .then(function(session) {
 return stripe.redirectToCheckout({ sessionId: session.id });
 })
 .then(function(result) {
 // If `redirectToCheckout` fails due to a browser or network
 // error, you should display the localized error message to your
 // customer using `error.message`.
 if (result.error) {
 alert(result.error.message);
 }
 })
 .catch(function(error) {
 console.error('Error:', error);
 });
 });
 */











































































 




 var stripe = Stripe('pk_test_51MDkyQDUzRcdw0ai84xqLsFylb0EVMCnP4Qv9y3NeW219gwQifI696lrqejOacOFEVO5bbIa3Zxd9bi5k7ON0sc200KlqO6jNm');

