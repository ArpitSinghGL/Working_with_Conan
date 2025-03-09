from conan import ConanFile

from conan.tools.cmake import cmake_layout

class FFmpegRecipe(ConanFile) :
    settings = "os" , "compiler" , "build_type" , "arch"
    generators = "CMakeToolchain" , "CMakeDeps"

    def requirements(self):
        self.requires("ffmpeg/7.0.1")

    def layout(self):
        cmake_layout(self)