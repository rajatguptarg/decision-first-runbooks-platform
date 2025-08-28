# Front-End Design Style

Follow the design language specified below for the front-end:

```
<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Decision First Runbook</title>
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;display=swap" rel="stylesheet"/>
<style>
        body {
            font-family: 'Inter', sans-serif;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800">
<div class="flex h-screen">
<aside class="w-96 bg-white p-6 border-r border-gray-200 flex flex-col">
<div class="relative mb-6">
<span class="material-icons absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">search</span>
<input class="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="Search runbooks" type="text"/>
</div>
<div class="bg-gray-800 text-white p-4 rounded-lg mb-4">
<div class="flex justify-between items-center">
<h3 class="font-semibold">API latency spike</h3>
<div class="relative inline-block w-10 mr-2 align-middle select-none transition duration-200 ease-in">
<input checked="" class="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer" id="toggle" name="toggle" type="checkbox"/>
<label class="toggle-label block overflow-hidden h-6 rounded-full bg-gray-300 cursor-pointer" for="toggle"></label>
</div>
</div>
<p class="text-sm text-gray-300">SRE Fire Brigade</p>
</div>
<div class="bg-white p-4 rounded-lg border border-gray-200 mb-6">
<h3 class="font-semibold text-gray-900">Credential leak suspected</h3>
<div class="flex justify-between items-center mt-2">
<p class="text-sm text-gray-500">Security Digital Detectives</p>
<span class="bg-gray-100 text-gray-600 text-xs font-medium px-2.5 py-0.5 rounded-full">SEV1</span>
</div>
</div>
<div class="bg-white p-4 rounded-lg border border-gray-200 flex-grow">
<div class="flex items-center mb-4">
<span class="material-icons text-gray-700 mr-3">format_list_bulleted</span>
<h3 class="font-semibold text-gray-900">Format checklist</h3>
</div>
<ul class="space-y-3 text-sm text-gray-600 list-disc list-inside">
<li>Start with a single decision question</li>
<li>Limit quick checks to five items</li>
<li>Surface the three most common branches</li>
<li>Put pitfalls next to actions</li>
<li>Link to deeper docs only when needed</li>
</ul>
</div>
</aside>
<main class="flex-1 p-8 overflow-y-auto">
<div class="space-y-6">
<div class="bg-white p-6 rounded-lg border border-gray-200">
<div class="flex justify-between items-center mb-4">
<div class="flex items-center">
<span class="material-icons text-gray-700 mr-3">schema</span>
<h2 class="text-lg font-semibold text-gray-900">Decision path</h2>
</div>
<button class="text-sm font-medium text-blue-600 hover:text-blue-800">Reset</button>
</div>
<div class="flex items-center space-x-4">
<p class="font-medium">Spike confirmed. Is error rate also elevated?</p>
<button class="flex items-center px-4 py-2 border border-gray-300 rounded-lg bg-white hover:bg-gray-50">
<span class="material-icons text-green-500 mr-2">check</span>
                            Yes
                        </button>
<button class="flex items-center px-4 py-2 border border-gray-300 rounded-lg bg-white hover:bg-gray-50">
<span class="material-icons text-red-500 mr-2">close</span>
                             No
                        </button>
</div>
</div>
<div class="bg-white p-6 rounded-lg border border-gray-200">
<div class="flex items-center mb-4">
<span class="material-icons text-orange-500 mr-3">warning_amber</span>
<h2 class="text-lg font-semibold text-gray-900">Pitfalls</h2>
</div>
<ul class="space-y-2 text-gray-600 list-disc list-inside">
<li>Do not restart all pods at once. Use rolling restart to avoid thundering herd</li>
<li>Warm up caches before shifting traffic back</li>
<li>If DB connections rise over 85 percent, increase pool only after verifying query plans</li>
</ul>
</div>
<div class="bg-white p-6 rounded-lg border border-gray-200">
<div class="flex justify-between items-start mb-4">
<div class="flex items-center">
<span class="material-icons text-gray-700 mr-3">visibility</span>
<h2 class="text-lg font-semibold text-gray-900">Overview</h2>
</div>
</div>
<div class="flex items-center space-x-2 mb-4">
<span class="bg-red-100 text-red-800 text-xs font-medium px-2.5 py-0.5 rounded-full">SEV2</span>
<span class="text-sm text-gray-500">Owner <span class="font-medium text-gray-800">SRE Fire Brigade</span></span>
<span class="text-sm text-gray-500">Updated <span class="font-medium text-gray-800">2025-07-18</span></span>
</div>
<div class="mb-4">
<h4 class="font-medium text-gray-900 mb-1">Objective</h4>
<p class="text-gray-600">Restore p95 latency under 300 ms within 15 minutes</p>
</div>
<div class="mb-4">
<h4 class="font-medium text-gray-900 mb-1">SLIs</h4>
<ul class="list-disc list-inside text-gray-600 space-y-1">
<li>p95 latency &lt; 300 ms</li>
<li>Error rate &lt; 1 percent</li>
<li>Traffic success &gt; 99 percent</li>
</ul>
</div>
<div>
<h4 class="font-medium text-gray-900 mb-1">Contacts</h4>
<ul class="list-disc list-inside text-gray-600 space-y-1">
<li>Incident Commander: @rajat.gupta712</li>
<li>Oncall SRE: @fire-brigade-oncall</li>
<li>Security Liaison: @digital-detectives</li>
</ul>
</div>
</div>
<div class="bg-white p-6 rounded-lg border border-gray-200">
<div class="flex items-center mb-4">
<span class="material-icons text-gray-700 mr-3">check_circle_outline</span>
<h2 class="text-lg font-semibold text-gray-900">Quick checks</h2>
</div>
<div class="space-y-3">
<div class="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
<p class="text-sm text-gray-800">Is the spike isolated to one region?</p>
<button class="flex items-center text-sm text-gray-500 hover:text-gray-700">
<span class="material-icons mr-1 text-base">content_copy</span>
                                Copy
                            </button>
</div>
<div class="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
<p class="text-sm text-gray-800">Is error rate rising too?</p>
<button class="flex items-center text-sm text-gray-500 hover:text-gray-700">
<span class="material-icons mr-1 text-base">content_copy</span>
                                Copy
                            </button>
</div>
<div class="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
<p class="text-sm text-gray-800">Any deploy in last 30 minutes?</p>
<button class="flex items-center text-sm text-gray-500 hover:text-gray-700">
<span class="material-icons mr-1 text-base">content_copy</span>
                                Copy
                            </button>
</div>
</div>
</div>
<div class="bg-white p-6 rounded-lg border border-gray-200">
<div class="flex items-center mb-4">
<span class="material-icons text-gray-700 mr-3">timeline</span>
<h2 class="text-lg font-semibold text-gray-900">Timeline</h2>
</div>
<div class="flex items-center space-x-2 mb-4">
<button class="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
<span class="material-icons mr-2 text-base">play_arrow</span>
                            Start
                        </button>
<button class="flex items-center px-4 py-2 border border-gray-300 rounded-lg bg-white hover:bg-gray-50">
<span class="material-icons mr-2 text-base">pause</span>
                            Pause
                        </button>
</div>
<p class="text-sm text-gray-500">No actions yet</p>
</div>
</div>
</main>
</div>
<style>
    .toggle-checkbox:checked {
        right: 0;
        border-color: #4f46e5;
    }
    .toggle-checkbox:checked + .toggle-label {
        background-color: #4f46e5;
    }
</style>

</body></html>
```