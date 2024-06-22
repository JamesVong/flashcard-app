/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["./src/*.{html,js}","./src/**/*.{html,js}"],
    
    theme: {
        colors: {
            transparent: 'transparent',
            primary: '#39BD72',
            secondary:'#414163',
            accent:'#61BE6B',
            background:'#141415',
          },
        fontFamily: {
            raleway: ['Raleway', 'sans-serif'],
        },
        extend: {
            
        },
    },
    plugins: [],
}