var icon = document.getElementById("icon")

icon.onclick = function () {
    document.body.classList.toggle("dark-theme");
    if (document.body.classList.contains("dark-theme")) {
        icon.src = "https://res.cloudinary.com/dsq1kzjdy/image/upload/v1654969324/icons/sun_wbtzoy.png";

    } else {
        icon.src = "https://res.cloudinary.com/dsq1kzjdy/image/upload/v1654969324/icons/moon_dx4nyu.png";
    }
}