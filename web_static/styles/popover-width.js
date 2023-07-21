function setPoPover() {
    const locations = document.querySelector('.locations');
    const locationsPopover = document.querySelector('locations.popover');

    const LocationsWidth = getComputedStyle(locations).width;
    locationsPopover.style.width = LocationsWidth
}

window.addEventListener('resize', setPoPover);