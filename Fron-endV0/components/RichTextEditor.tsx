'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Bold, Italic, List, Heading2 } from 'lucide-react'

interface RichTextEditorProps {
  value: string
  onChange: (value: string) => void
  placeholder?: string
  minHeight?: string
}

export function RichTextEditor({
  value,
  onChange,
  placeholder = 'Share your professional experience...',
  minHeight = 'min-h-48',
}: RichTextEditorProps) {
  const [isFocused, setIsFocused] = useState(false)

  const formatText = (before: string, after: string = '') => {
    const textarea = document.querySelector(
      '[data-rich-editor]'
    ) as HTMLTextAreaElement
    if (!textarea) return

    const start = textarea.selectionStart
    const end = textarea.selectionEnd
    const selectedText = value.substring(start, end)
    const beforeText = value.substring(0, start)
    const afterText = value.substring(end)

    const newValue =
      beforeText + before + selectedText + after + afterText
    onChange(newValue)

    // Reset cursor position
    setTimeout(() => {
      textarea.focus()
      textarea.selectionStart = start + before.length
      textarea.selectionEnd = start + before.length + selectedText.length
    }, 0)
  }

  return (
    <div className="space-y-3">
      {/* Toolbar */}
      <div className="flex gap-2 p-3 border border-border rounded-lg bg-muted/30">
        <Button
          type="button"
          variant="ghost"
          size="sm"
          onClick={() => formatText('**', '**')}
          title="Bold"
          className="h-9 w-9 p-0"
        >
          <Bold className="w-4 h-4" />
        </Button>
        <Button
          type="button"
          variant="ghost"
          size="sm"
          onClick={() => formatText('_', '_')}
          title="Italic"
          className="h-9 w-9 p-0"
        >
          <Italic className="w-4 h-4" />
        </Button>
        <Button
          type="button"
          variant="ghost"
          size="sm"
          onClick={() => formatText('- ')}
          title="Bullet List"
          className="h-9 w-9 p-0"
        >
          <List className="w-4 h-4" />
        </Button>
        <Button
          type="button"
          variant="ghost"
          size="sm"
          onClick={() => formatText('## ')}
          title="Heading"
          className="h-9 w-9 p-0"
        >
          <Heading2 className="w-4 h-4" />
        </Button>
      </div>

      {/* Editor */}
      <textarea
        data-rich-editor
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
        placeholder={placeholder}
        className={`w-full ${minHeight} p-4 border rounded-lg bg-background text-foreground placeholder-muted-foreground resize-none focus:outline-none focus:ring-2 focus:ring-primary/50 transition-all ${
          isFocused ? 'border-primary' : 'border-border'
        }`}
      />

      {/* Character count */}
      <div className="text-xs text-muted-foreground text-right">
        {value.length} characters
      </div>
    </div>
  )
}
