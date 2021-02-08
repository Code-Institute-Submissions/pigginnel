function initMap() {
    // The location of Pig in a Ginnel
    const restaurant = { lat: 51.51082318227617, lng: -0.12201741048441295 };
    // The map, centered at the restaurant
    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 15,
      center: restaurant,
    });
    // The marker, positioned at Pig in a Ginnel
    const marker = new google.maps.Marker({
      position: restaurant,
      map: map,
    });
  }
