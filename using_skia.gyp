{
  'targets': [
    {
      'configurations': {
        'Debug': { },
        'Release': { }
      },
      'target_name': 'appels',
      'type': 'executable',
      'dependencies': [
        'third_party/skia/skia.gyp:alltargets',
        'third_party/skia/gyp/sdl.gyp:sdl',
      ],
      'include_dirs': [
        'third_party/skia/include/config',
        'third_party/skia/include/core',
        'third_party/skia/include/gpu',
        'third_party/skia/include/gpu/gl',
        'third_party/skia/include/utils',
        'third_party/skia/third_party/externals/sdl/include',
        'third_party/skia/src/gpu/',
      ],
      'sources': [
        'app/appels.cpp'
      ],
      'ldflags': [
        '-std=c++11',
      ],
      'cflags': [
        '-Werror', '-W', '-Wall', '-Wextra', '-Wno-unused-parameter', '-g', '-O0'
      ]
    }
  ]
}
