import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'


// https://vitejs.dev/config/
// https://github.com/vitejs/vite/discussions/6552#discussioncomment-2002155
export default defineConfig(({ command, mode, ssrBuild }) => {
  if (command === 'build') {
    return {

      plugins: [react({
        exclude: /\.stories\.(t|j)sx?$/,
        include: '**/*.(ts|tsx)',
      })],
      base: "/static/",
      publicDir: './public',
      build: {
        // https://rollupjs.org/configuration-options/#output-amd-basepath
        rollupOptions: {
          // basePath: "/static/",
          output: {
            chunkFileNames: 'assets/js/[name]-[hash].js',
            entryFileNames: 'assets/js/[name]-[hash].js',
            assetFileNames: ({name}) => {
              if (/\.(gif|jpe?g|png|svg)$/.test(name ?? '')){
                  return 'assets/images/[name]-[hash][extname]';
              }
              if (/\.css$/.test(name ?? '')) {
                  return 'assets/css/[name]-[hash][extname]';   
              }
              // default value
              // ref: https://rollupjs.org/guide/en/#outputassetfilenames
              return 'assets/[name]-[hash][extname]';
            },
          },
        }    
      }

    }
  }

  else {
    return {
      plugins: [react({
        exclude: /\.stories\.(t|j)sx?$/,
        include: '**/*.(ts|tsx)',
      })],
      publicDir: './public',
      build: {
        rollupOptions: {
          output: {
            chunkFileNames: 'assets/js/[name]-[hash].js',
            entryFileNames: 'assets/js/[name]-[hash].js',
            assetFileNames: ({name}) => {
              if (/\.(gif|jpe?g|png|svg)$/.test(name ?? '')){
                  return 'assets/images/[name]-[hash][extname]';
              }
              if (/\.css$/.test(name ?? '')) {
                  return 'assets/css/[name]-[hash][extname]';   
              }
              return 'assets/[name]-[hash][extname]';
            },
          },
        }    
      }

    }
  }

})
