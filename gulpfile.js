'use strict';

const gulp = require('gulp');
const sass = require('gulp-sass');
const postcss = require('gulp-postcss');
const concat = require('gulp-concat')
const cleanCSS = require('gulp-clean-css');//To Minify CSS files
const purgecss = require('gulp-purgecss');// Remove Unused CSS from Styles
const del = require('del'); //For Cleaning build/dist for fresh export

const root_input = './static_src/';
const root_output = './static/';

const refresh = require('gulp-refresh');
const {build} = require('esbuild')


gulp.task('dev_ts', async () => {
    await build({
      entryPoints: [root_input + 'ts/main.ts'],
      outfile: root_output + 'js/main.js',
      minify: false,
      bundle: true,
      sourcemap: false,
    })
    await refresh.reload(root_output + 'js/main.js')
  }
);

gulp.task('prod_ts', async () => {
    await build({
      entryPoints: [root_input + 'ts/main.ts'],
      outfile: root_output + 'js/main.js',
      minify: true,
      bundle: true,
      sourcemap: true,
    })
  }
);

gulp.task('prod_vendor', async () => {
  await build({
    entryPoints: [root_input + 'vendor/vendor.js'],
    outfile: root_output + 'js/vendor.js',
    minify: true,
    bundle: true,
    sourcemap: true,
  })
})

gulp.task('dev_vendor', async () => {
  await build({
    entryPoints: [root_input + 'vendor/vendor.js'],
    outfile: root_output + 'js/vendor.js',
    minify: false,
    bundle: true,
    sourcemap: false,
  })
})

gulp.task('dev_styles', function () {
  const tailwindcss = require('tailwindcss');
  return gulp.src(root_input + "sass/base.scss")
    .pipe(sass().on('error', sass.logError))
    .pipe(postcss([
      tailwindcss('tailwind.config.js'),
      require('autoprefixer'),
    ]))
    .pipe(concat({path: 'style.css'}))
    .pipe(gulp.dest(root_output + "css"))
    .pipe(refresh());

});

gulp.task('prod_styles', function () {
  const tailwindcss = require('tailwindcss');
  return gulp.src(root_input + "sass/base.scss")
    // .pipe(sourcemaps.init())
    .pipe(sass().on('error', sass.logError))
    .pipe(postcss([
      tailwindcss('tailwind.config.js'),
      require('autoprefixer'),
    ]))
    .pipe(concat({path: 'style.css'}))
    .pipe(purgecss({
      content: ['templates/**/*.{html,js}'],
      defaultExtractor: content => {
        const broadMatches = content.match(/[^<>"'`\s]*[^<>"'`\s:]/g) || []
        const innerMatches = content.match(/[^<>"'`\s.()]*[^<>"'`\s.():]/g) || []
        return broadMatches.concat(innerMatches)
      }
    }))
    .pipe(cleanCSS())
    .pipe(gulp.dest(root_output + "css"))

});


function clean_css() {
  return del([root_output + "css"]);
}

function clean_js() {
  return del([root_output + "js"]);
}


gulp.task('watch', function () {
  refresh.listen();
  gulp.watch(root_input + "sass/**/*.scss", gulp.parallel(['dev_styles']));
  gulp.watch(root_input + "vendor/**/*.js", gulp.parallel(['dev_vendor']));
  gulp.watch(root_input + "ts/**/*.ts", gulp.parallel(['dev_ts']));
  gulp.watch("./templates/**/*.html").on("change", refresh.reload);
});

gulp.task('default', gulp.series(
  gulp.parallel([clean_css, clean_js]),
  gulp.parallel(['dev_styles', 'dev_ts', 'dev_vendor', 'watch',])
  )
);

gulp.task('prod', gulp.series(
  gulp.parallel([clean_css, clean_js]),
  gulp.parallel(['prod_styles', 'prod_ts', 'prod_vendor'])
  )
);
