(function() {
    'use strict';

    angular
        .module('blogapp.auth')
        .directive('uniqueEmail', uniqueEmail);

    uniqueEmail.$inject = ['API', '$http'];
    function uniqueEmail(API, $http) {
        var uniqueEmailDirective = {
            require: 'ngModel',
            restrict: 'EA',
            link: linkFunc
        };

        return uniqueEmailDirective;

        /** @ngInject */
        function linkFunc(scope, el, attr, ngModel) {
            var url = API + '/users/email';

            ngModel.$parsers.push(function(val) {
                if (!val || val.length == 0) {
                    ngModel.$setValidity('emailAvailability', true);
                    return;
                }
                ngModel.$setValidity('emailAvailability', false);

                var data = {email: val};

                $http.post(url, data)
                .then(function(response) {
                    ngModel.$setValidity('emailAvailability', true);
                }, function(response) {
                    ngModel.$setValidity('emailAvailability', false);
                });
                return val;
            });
        }

    }  // <-- uniqueEmail

})();
