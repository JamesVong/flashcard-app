import React from 'react';

function Register(){
    const msg = new URLSearchParams(window.location.search).get('message')
    console.log(msg);
    return (
        <div className="flex min-h-full items-center flex-col justify-center px-6 py-12 lg:px-8">
          <div className="w-full bg-slate-100 rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-4 ">

            <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                <form className="space-y-6" action="/api/register" method="POST">
                  <div>
                    <label for="email" className="block text-sm font-medium leading-6 text-gray-900">Email address</label>
                    <div className="mt-2">
                      <input id="email" name="email" type="email" autocomplete="email" required className="block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm bg-highlight bg-opacity-50 sm:text-sm sm:leading-6"/>
                    </div>
                  </div>

                  <div>
                    <div className="flex items-center justify-between">
                      <label for="password" className="block text-sm font-medium leading-6 text-gray-900">Password</label>
                      <div className="text-sm">
                        <a href="/forgot" className="font-semibold">Forgot password?</a>
                      </div>
                    </div>
                    <div className="mt-2">
                      <input id="password" name="pass" type="password" autocomplete="current-password" required className="block w-full rounded-md border-0 py-1.5 bg-highlight bg-opacity-50 shadow-sm sm:text-sm sm:leading-6"/>
                    </div>
                  </div>

                  <div>
                    <div className="flex items-center justify-between">
                      <label for="password" className="block text-sm font-medium leading-6 text-gray-900">Retype Password</label>
                    </div>
                    <div className="mt-2">
                      <input id="password" name="pass2" type="password" autocomplete="current-password" required className="block w-full rounded-md border-0 py-1.5 shadow-sm bg-highlight bg-opacity-50 sm:text-sm sm:leading-6"/>
                    </div>
                  </div>

                  <div className="pb-8">
                    <button type="submit" className="flex w-full justify-center rounded-md bg-primary px-3 py-1.5 text-sm font-semibold leading-6 shadow-sm">Sign in</button>
                    <p className="text-sm font-light text-gray-500 dark:text-gray-400">
                    Already have an account? <a href="/login" className="font-medium text-black hover:underline">Login</a>
                    </p>
                  </div>
                </form>
            </div>
          </div>
        </div>
    )
}
export default Register;