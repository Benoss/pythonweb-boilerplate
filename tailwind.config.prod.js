let tailwind_config = require("./tailwind.config");

tailwind_config.purge = {
  content: ["./templates/**/*.html", "./templates/**/*.js"],
  safelist: [],
};

module.exports = tailwind_config;
