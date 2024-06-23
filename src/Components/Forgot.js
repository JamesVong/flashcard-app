import React from 'react';

function ForgotPage(){
    
    return (
        <div className="flex min-h-full items-center flex-col justify-center px-6 py-12 lg:px-8">
            <div className="w-full bg-slate-100 rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-4">
                <div className="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
                <form className="space-y-6 " action="/api/forgot" method="POST">
                        
                        <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email</label>
                        <div className="mt-2">
                            <input id="email" name="email" type="email" autocomplete="email" required className="block rounded-md border-0 py-1.5 shadow-sm bg-highlight bg-opacity-50 sm:text-sm sm:leading-6"/>
                        </div>
                                    
                        <div class="pb-8">
                            <button type="submit" className="flex w-full justify-center rounded-md bg-primary px-3 py-1.5 text-sm font-semibold leading-6 shadow-sm">Sign in</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    )
}

export default ForgotPage;