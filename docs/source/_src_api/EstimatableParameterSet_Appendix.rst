The :class:`EstimatableParameterSet` object contains three objects that have :class:`EstimatableParameter` as base class (one for each parameter). We distinguish two types of :class:`EstimatableParameter` objects:

* Those that represent initial conditions for dynamics (denoted as :math:`\mathbf{x}_{0}` below)
* Those that represent fixed parameters for environment, acceleration or observation models (denoted as :math:`\mathbf{q}` below)

Resetting the full parameter vector :math:`\mathbf{p}(=[\mathbf{x}_{0};\mathbf{q}])` is done as follows (for :literal:`double` state scalar type):

   .. code-block:: cpp

       // Create parameter set
       std::shared_ptr< EstimatableParameterSet< double > > parametersToEstimate = ...

       Eigen::VectorXd parameterVector =
            parametersToEstimate->getFullParameterValues< double >( );

While resetting the full parameter vector is done as:

   .. code-block:: cpp

       // Create parameter set
       std::shared_ptr< EstimatableParameterSet< double > > parametersToEstimate = ...

       // Define vector of new values of estimated parameters
       Eigen::VectorXd newParameterVector = ...

       // Reset parameter values
       parametersToEstimate->resetParameterValues< double >( );

When resetting the parameter vector, the change in the values in :math:`\mathbf{q}` immediately take effect. For the initial state parameters to take effect, however, the dynamics must be re-propagated. This occurs automatically when estimating parameters. It can also be performed manually by calling the :literal:`resetParameterEstimate` member function of the :class:`VariationalEquationsSolver` class.

