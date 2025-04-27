module.exports = {
    content: ['./pages/**/*.{js,jsx}', './components/**/*.{js,jsx}'],
    theme: {
      extend: {
        animation: {
          'fade-in': 'fadeIn 1s ease-out',
          'fade-in-slow': 'fadeIn 2s ease-out',
          'bounce-slow': 'bounce 2s infinite',
        },
        keyframes: {
          fadeIn: {
            '0%': { opacity: 0, transform: 'translateY(20px)' },
            '100%': { opacity: 1, transform: 'translateY(0)' },
          },
        },
      },
    },
    plugins: [],
  }
  