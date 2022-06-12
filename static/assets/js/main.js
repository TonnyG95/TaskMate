function darkmode() {
    var SetTheme = document.body;
    SetTheme.classList.toggle("dark-theme")
    var theme;
    if (SetTheme.classList.contains("dark-theme")) {
        console.log("Dark mode");
        theme = "DARK";
    } else {
        console.log("Light mode");
        theme = "LIGHT";
    }
    // save to localStorage
    localStorage.setItem("PageTheme", JSON.stringify(theme));
    // ensure you convert to JSON like i have done -----JSON.stringify(theme)
}

setInterval(() => {
    let GetTheme = JSON.parse(localStorage.getItem("PageTheme"));
    console.log(GetTheme);
    if (GetTheme === "DARK") {
        document.body.classList = "dark-theme";
    } else {
        document.body.classList = "";
    }

    if (document.body.classList.contains("dark-theme")) {
        icon.src = "https://res.cloudinary.com/dsq1kzjdy/image/upload/v1654969324/icons/sun_wbtzoy.png";

    } else {
        icon.src = "https://res.cloudinary.com/dsq1kzjdy/image/upload/v1654969324/icons/moon_dx4nyu.png";
    }
}, 5);