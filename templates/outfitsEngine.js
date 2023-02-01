// create an engine to display the outfits to wear based on the conditions pulled from the API

// inputs: temperature(farenheit) and precipitation(boolean) pulled from the api

//hot outfit
const hotOutfit = {
    top: "T-Shirt",
    bottom: "Shorts",
    footwear: "Sandals",
}

const hotWetOutfit = {
    top: "T-Shirt",
    bottom: "Shorts",
    footwear: "Sandals",
    Accessories: "Umbrella"
}

const coldOutfit = {
    top: "Hoodie",
    bottom: "Jeans",
    footwear: "Tennis shoes",
}

const coldWetOutfit = {
    top: "Hoodie",
    bottom: "Jeans",
    footwear: "Tennis shoes",
    Accessories: "Umbrella"
}

const warmOutfit = {
    top: "T-Shirt",
    bottom: "Jeans",
    footwear: "Tennis shoes",
}

const warmWetOutfit = {
    top: "T-Shirt",
    bottom: "Jeans",
    footwear: "Tennis shoes",
    Accessories: "Umbrella"
}



function outfitGenerator(temp, precip)
    // hot and dry
    //Input: hot, precip = false
    //output: hot outfit
    if (temp === "hot" && precip == false) {
    document.getElementById("hotOutfit").innerHTML = `
    It's hot out today!
    <div>
        <p>Today you should wear:</p>
        <li>T-Shirt</li>
        <li>Shorts</li>
        <li>Sandals</li>
    </div>
    `;
    // hot and wet
    } else if (temp === "hot" && precip == true) {
        document.getElementById("hotWetOutfit").innerHTML = `
        <h1>It's hot out today!</h1>
        <div>
        <!-- Top, bottom, footwear for hot rainy weather -->
        <p>Today you should wear:</p>
        <li>T-Shirt</li>
        <li>Shorts</li>
        <li>Sandals</li>
        <!-- Accessories -->
        <p>Accessories you may want to bring with you:</p>
        <li>Umbrella</li>
        </div>
        `;

        // cold and dry
        }else if (temp === "cold" && precip == false) {
    document.getElementById("coldOutfit").innerHTML = `
    <h1>It's cold out today!</h1>
    <div>
        <p>Today you should wear:</p>
        <li>Hoodie</li>
        <li>Jeans</li>
        <li>Tennis Shoes</li>
    </div>
    `;
    // cold and wet
    } else if (temp === "cold" && precip == true) {
        document.getElementById("coldWetOutfit").innerHTML = `
        <h1>It's cold and wet out today!</h1>
        <div>
    // Top, bottom, footwear for hot rainy weather
        <p>Today you should wear:</p>
        <li>Hoodie</li>
        <li>Jeans</li>
        <li>Tennis Shoes</li>
        <!-- Accessories -->
        <p>Accessories you may want to bring with you:</p>
        <li>Umbrella</li>
        </div>
        `;
        // warm and dry
        }else if (temp === "warm" && precip == false) {
    document.getElementById("warmDryOutfit").innerHTML = `
    <h1>It's warm out today!</h1>
    <div>
        <p>Today you should wear:</p>
        <li>T-shirt</li>
        <li>Jeans</li>
        <li>Tennis Shoes</li>
    </div>
    `;
    // warm and wet
    }else if (temp === "warm" && precip == true) {
        document.getElementById("warmWetOutfit").innerHTML = `
        <h1>It's warm and wet out today!</h1>
        <div>
            <p>Today you should wear:</p>
            <li>T-Shirt</li>
            <li>Jeans</li>
            <li>Tennis Shoes</li>
            <!-- Accessories -->
            <p>Accessories you may want to bring with you:</p>
            <li>Umbrella</li>
        </div>
    `;
    }

 // make some mock data, like tits above, and that drives conditions
  // the conditions are if/elses that are determine what to wear based on mock data
  // you need to think about the data structure to use for showing random clothing shit
  // see white board for some basic shit/ideas 