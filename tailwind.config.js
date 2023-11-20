/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.{html,js}"],
  theme: {
    fontFamily: {
      'body': ['Jost', 'Arial', 'Helvetica'],
      'awesome': ['FontAwesome'],
    },
    container: {
      screens: {
        sm: '640px',
        md: '768px',
        lg: '1024px',
        xl: '1280px',
        xxl: '1400px',
        '3xl': '1790px',
      }
    },
    extend: {
      backgroundImage: {
        'payments_troy': "url('/static/images/payment/troy-logo-transparent.png')",
        'payments_visa': "url('/static/images/payment/footer-master-card.png')",
        'payments_master': "url('/static/images/payment/footer-visa-black.png')",
      },
      colors: {
        'black-m': '#333'
      }
      
    },
  },
  plugins: [],
}

