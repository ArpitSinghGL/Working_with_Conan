from conan import ConanFile

from conan.tools.cmake import CMake , cmake_layout , CMakeDeps , CMakeToolchain

class HelloPackageRecipe(ConanFile) :
    settings = "os" , "compiler" , "build_type" , "arch"
    generators = "CMakeToolchain" , "CMakeDeps"

    def requirements(self):
        self.requires("hello/1.0")

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()