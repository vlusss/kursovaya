function calculate_total_price(){
    const total_el = document.getElementById("total_price")
    const rent_el = document.getElementById("id_rent_time")
    const price_el = document.getElementById("car_price")
    const MINUTES_IN_HOUR = 60
    total_el.value = ((rent_el.value / MINUTES_IN_HOUR) * parseInt(price_el.innerText) +
        (rent_el.value % MINUTES_IN_HOUR) * (parseInt(price_el.innerText) / MINUTES_IN_HOUR)).toFixed(2)
}
