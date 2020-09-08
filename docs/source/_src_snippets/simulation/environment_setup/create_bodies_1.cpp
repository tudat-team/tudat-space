// load spice kernels
spice_interface::load_standard_spice_kernels()

// define bodies in simulation
std::vector<std::string> bodiesToCreate = {"Sun", "Earth", "Moon"};

// create body settings map
std::map<std::string, std::shared_ptr<BodySettings>> bodySettings =
    getDefaultBodySettings(bodiesToCreate);

// create body system object
NamedBodyMap bodyMap = createBodies(bodySettings);
